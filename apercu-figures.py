#!/usr/bin/env python3
"""Montre les figures des exercices : celles en place, et celles qui manquent.

    python3 apercu-figures.py          → tous les chapitres
    python3 apercu-figures.py 25       → un seul

Le fichier produit contient du contenu privé : il est ignoré par git.
"""
import base64, csv, html, json, os, re, subprocess, sys, webbrowser

DEPOT = "lesmaths1200/lesmaths1200-prive"
CACHE = os.path.expanduser("~/.cache/maths1200-figures")


def api(chemin):
    return subprocess.run(["gh", "api", f"repos/{DEPOT}/contents/{chemin}", "--jq", ".content"],
                          capture_output=True, text=True, check=True).stdout


def figure_locale(nom):
    """Télécharge la figure une fois, pour que la page s'affiche hors ligne."""
    os.makedirs(CACHE, exist_ok=True)
    chemin = os.path.join(CACHE, nom)
    if not os.path.exists(chemin):
        with open(chemin, "wb") as f:
            f.write(base64.b64decode(api(f"exercices/figures/{nom}")))
    return chemin


ex = json.loads(base64.b64decode(api("exercices/exercices.json")))
posees = {e["name"] for e in json.loads(subprocess.run(
    ["gh", "api", f"repos/{DEPOT}/contents/exercices/figures"],
    capture_output=True, text=True, check=True).stdout)}
with open("cours.csv", encoding="utf-8") as f:
    noms = {r["id"]: r["titre"] for r in csv.DictReader(f, delimiter=";")}

cles = sys.argv[1:] or sorted((k for k in ex if k.isdigit()), key=int)
s = ["""<!doctype html><meta charset="utf-8"><title>Figures des exercices</title>
<script>window.MathJax={tex:{inlineMath:[['$','$']]}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
 body{font:16px/1.6 -apple-system,system-ui,sans-serif;max-width:900px;margin:2rem auto;
      padding:0 1rem;color:#1a1a1a}
 h1{font-size:1.5rem} h2{margin-top:2.6rem;border-top:2px solid #111;padding-top:.8rem}
 .ex{border:1px solid #ddd;border-radius:10px;padding:.85rem 1.05rem;margin:.9rem 0}
 .manque{border-color:#d08a3e;background:#fdf6ee}
 .nom{float:right;font-family:ui-monospace,monospace;font-size:.8rem;background:#111;
      color:#fff;padding:.18rem .5rem;border-radius:5px}
 .manque .nom{background:#b5701f}
 .num{font-weight:700;color:#555;font-size:.9rem}
 .enonce{margin:.45rem 0;white-space:pre-wrap}
 img{max-width:100%;border:1px solid #e3e3e3;border-radius:8px;margin-top:.5rem}
 .desc{color:#666;font-size:.88rem;margin-top:.4rem}
 .intro{background:#f6f6f6;border-radius:9px;padding:.9rem 1.1rem}
 .bilan{background:#eef6ee;border-radius:9px;padding:.9rem 1.1rem;margin-top:2rem}
</style>
<h1>Figures des exercices</h1>
<div class='intro'>Chaque exercice ci-dessous comporte une figure. Celles qui sont
<b>en place</b> s'affichent telles que l'élève les voit dans l'application. Celles qui
<b>manquent</b> apparaissent sur fond orange, avec le nom de fichier à donner : dépose-les
dans le dépôt privé, sous <code>exercices/figures/</code>.</div>"""]

enplace = manquent = 0
for cle in cles:
    fiche = ex.get(str(cle))
    if not isinstance(fiche, dict) or "exercices" not in fiche: continue
    lignes, n_ok, n_ko = [], 0, 0
    for e in fiche["exercices"]:
        enonce, numero = e["enonce"], e["numero"]
        nom = f"fiche{cle}-ex{numero}.jpg"
        # « [Figure : description | fichier.jpg] », crochets internes compris
        m = None
        i = enonce.find("[Figure")
        if i >= 0:
            n = 0
            for j in range(i, len(enonce)):
                if enonce[j] == "[": n += 1
                elif enonce[j] == "]":
                    n -= 1
                    if n == 0:
                        marqueur = enonce[i:j+1]
                        f2 = re.search(r"\|\s*([^\s|\]]+\.jpg)\s*\]$", marqueur)
                        if f2:
                            desc = marqueur[len("[Figure"):f2.start()].lstrip(" :").strip()
                            m = (marqueur, f2.group(1), desc)
                        break
        attend = i >= 0 and m is None
        if not m and not attend: continue
        corps = [f"<span class='num'>Exercice {numero}</span>"]
        if m:
            n_ok += 1
            texte = enonce.replace(m[0], "").strip()
            corps.append(f"<span class='nom'>{m[1]}</span>")
            corps.append(f"<div class='enonce'>{texte}</div>")
            corps.append(f"<img src='file://{figure_locale(m[1])}'>")
            if m[2]:
                corps.append(f"<div class='desc'><b>VoiceOver :</b> {html.escape(m[2])}</div>")
            lignes.append("<div class='ex'>" + "".join(corps) + "</div>")
        else:
            n_ko += 1
            d = re.search(r"\[Figure\s*:?\s*(.*?)\]", enonce, re.S)
            texte = re.sub(r"\[Figure.*?\]", "", enonce, flags=re.S).strip()
            corps.append(f"<span class='nom'>{nom} — à fournir</span>")
            corps.append(f"<div class='enonce'>{texte}</div>")
            corps.append(f"<div class='desc'><b>Figure attendue :</b> "
                         f"{html.escape(d.group(1).strip()) if d else '—'}</div>")
            lignes.append("<div class='ex manque'>" + "".join(corps) + "</div>")
    if not lignes: continue
    enplace += n_ok; manquent += n_ko
    etat = f"{n_ok} en place" + (f", <b>{n_ko} à fournir</b>" if n_ko else "")
    s.append(f"<h2>{html.escape(noms.get(str(cle), cle))} — {etat}</h2>")
    s.extend(lignes)

s.append(f"<div class='bilan'><b>{enplace} figures en place</b>"
         + (f", <b>{manquent} encore à fournir</b>." if manquent
            else ", et plus aucune ne manque.") + "</div>")
with open("apercu-figures.html", "w", encoding="utf-8") as f:
    f.write("\n".join(s))
print(f"  {enplace} en place, {manquent} à fournir → apercu-figures.html")
webbrowser.open("file://" + os.path.abspath("apercu-figures.html"))
