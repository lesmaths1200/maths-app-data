#!/usr/bin/env python3
"""Liste les figures à fournir, chapitre par chapitre, avec leur nom de fichier.

    python3 apercu-figures.py          → tous les chapitres
    python3 apercu-figures.py 25       → un seul

Le fichier produit contient du contenu privé : il est ignoré par git.
"""
import base64, csv, html, json, os, re, subprocess, sys, webbrowser

DEPOT = "lesmaths1200/lesmaths1200-prive"


def lire(chemin):
    out = subprocess.run(["gh", "api", f"repos/{DEPOT}/contents/{chemin}", "--jq", ".content"],
                         capture_output=True, text=True, check=True).stdout
    return json.loads(base64.b64decode(out))


def nom_fichier(cle, numero):
    return f"fiche{cle}-ex{numero}.jpg"


ex, noms = lire("exercices/exercices.json"), {}
with open("cours.csv", encoding="utf-8") as f:
    noms = {r["id"]: r["titre"] for r in csv.DictReader(f, delimiter=";")}

cles = sys.argv[1:] or sorted(ex, key=int)
s = ["""<!doctype html><meta charset="utf-8"><title>Figures à fournir</title>
<script>window.MathJax={tex:{inlineMath:[['$','$']]}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
 body{font:16px/1.6 -apple-system,system-ui,sans-serif;max-width:860px;margin:2rem auto;
      padding:0 1rem;color:#1a1a1a}
 h1{font-size:1.5rem} h2{margin-top:2.4rem;border-top:2px solid #111;padding-top:.8rem}
 .ex{border:1px solid #ddd;border-radius:10px;padding:.85rem 1.05rem;margin:.8rem 0}
 .nom{float:right;font-family:ui-monospace,monospace;font-size:.82rem;background:#111;
      color:#fff;padding:.18rem .5rem;border-radius:5px}
 .num{font-weight:700;color:#555;font-size:.9rem}
 .enonce{margin:.45rem 0;white-space:pre-wrap}
 .fig{background:#fdf4ec;border-left:3px solid #d08a3e;padding:.5rem .8rem;margin-top:.5rem;
      font-size:.93rem}
 .intro{background:#f6f6f6;border-radius:9px;padding:.9rem 1.1rem}
</style>
<h1>Figures à fournir</h1>
<div class='intro'>Chaque exercice ci-dessous attend une figure. Le <b>nom de fichier</b> à
donner est indiqué en haut à droite, en noir. Dépose les images dans le dépôt privé, sous
<code>exercices/figures/</code> : l'app les téléchargera d'elle-même, sans nouvelle version.
<br><br>Le format importe peu — photo, capture ou découpe du PDF. Vise une largeur d'au moins
800 pixels, en JPEG.</div>"""]

total = 0
for cle in cles:
    fiche = ex.get(str(cle))
    if not fiche: continue
    avec = [e for e in fiche["exercices"] if "[Figure" in e["enonce"]]
    if not avec: continue
    s.append(f"<h2>{html.escape(noms.get(str(cle), cle))} — {len(avec)} figures</h2>")
    for e in avec:
        total += 1
        fig = re.search(r"\[Figure\s*:?\s*(.*?)\]", e["enonce"], re.S)
        enonce = re.sub(r"\[Figure.*?\]", "", e["enonce"], flags=re.S).strip()
        s.append("<div class='ex'>")
        s.append(f"<span class='nom'>{nom_fichier(cle, e['numero'])}</span>")
        s.append(f"<span class='num'>Exercice {e['numero']}</span>")
        s.append(f"<div class='enonce'>{enonce}</div>")
        s.append(f"<div class='fig'><b>Figure attendue :</b> {html.escape(fig.group(1).strip()) if fig else '—'}</div>")
        s.append("</div>")

s.append(f"<p class='intro'>{total} figures au total.</p>")
with open("apercu-figures.html", "w", encoding="utf-8") as f:
    f.write("\n".join(s))
print(f"  {total} figures → apercu-figures.html")
webbrowser.open("file://" + os.path.abspath("apercu-figures.html"))
