#!/usr/bin/env python3
"""Les exercices masqués qui attendent un tableau, une grille ou un tracé.

Distinct des figures géométriques : ici l'image à fournir est une mise en
page — un tableau à remplir, deux colonnes à relier, une grille — et non le
dessin d'une figure.

    python3 apercu-tableaux.py
"""
import base64, csv, html, json, os, re, subprocess, webbrowser

DEPOT = "lesmaths1200/lesmaths1200-prive"
d = json.loads(base64.b64decode(subprocess.run(
    ["gh", "api", f"repos/{DEPOT}/contents/exercices/exercices.json", "--jq", ".content"],
    capture_output=True, text=True, check=True).stdout))
with open("cours.csv", encoding="utf-8") as f:
    t = {r["id"]: r["titre"] for r in csv.DictReader(f, delimiter=";")}


def bloc(x, depart):
    """Le marqueur complet, crochets internes compris."""
    i = x.find(depart)
    if i < 0: return None
    n = 0
    for j in range(i, len(x)):
        if x[j] == "[": n += 1
        elif x[j] == "]":
            n -= 1
            if n == 0: return x[i:j+1]
    return None


def tous_les_blocs(x):
    """Tous les marqueurs « [Tableau … ] » et « [Figure … ] » de l'énoncé."""
    blocs, i = [], 0
    while True:
        deb = min((p for p in (x.find("[Tableau", i), x.find("[Figure", i)) if p >= 0), default=-1)
        if deb < 0: return blocs
        n = 0
        for j in range(deb, len(x)):
            if x[j] == "[": n += 1
            elif x[j] == "]":
                n -= 1
                if n == 0:
                    blocs.append(x[deb:j+1]); i = j + 1; break
        else:
            return blocs


MISE_EN_PAGE = re.compile(r"tableau|grille|colonnes? \d|a relier|à relier|relier", re.I)
attente, douteux = [], []
for cle, f in d.items():
    if not isinstance(f, dict) or "exercices" not in f: continue
    for e in f["exercices"]:
        x, nom = e["enonce"], f"fiche{cle}-ex{e['numero']}.jpg"
        # chaque marqueur de l'énoncé, et non le premier seulement : un
        # exercice peut attendre une figure tout en en ayant déjà une.
        for m in tous_les_blocs(x):
            if re.search(r"\|\s*[^\s|\]]+\.jpg\s*\]$", m): continue   # déjà reliée
            desc = re.sub(r"\s+", " ", m.lstrip("[").split(":", 1)[-1].rstrip("]")).strip()
            if not (m.startswith("[Tableau") or MISE_EN_PAGE.search(desc)): continue
            # le nom voulu peut être indiqué dans la description
            attendu = re.search(r"\(a fournir : ([^)]+)\)", desc)
            # deux marqueurs dans le même exercice ne peuvent pas porter le
            # même nom de fichier : on les suffixe a, b, c…
            rang = sum(1 for a in attente if a[1] == e["numero"] and a[0] == t.get(cle, cle))
            defaut = nom if rang == 0 else nom.replace(".jpg", f"{chr(97+rang)}.jpg")
            fichier = attendu.group(1) if attendu else defaut
            propre = desc.replace(attendu.group(0), "").strip() if attendu else desc
            attente.append((t.get(cle, cle), e["numero"], fichier,
                            x.replace(m, "").strip(), propre))

s = ["""<!doctype html><meta charset="utf-8"><title>Tableaux à fournir</title>
<script>window.MathJax={tex:{inlineMath:[['$','$']]}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>body{font:16px/1.6 -apple-system,system-ui,sans-serif;max-width:880px;margin:2rem auto;
padding:0 1rem}h2{margin-top:2.4rem;border-top:2px solid #111;padding-top:.8rem;font-size:1.15rem}
.ex{border:1px solid #9bb7d4;background:#f2f7fc;border-radius:10px;padding:.85rem 1.05rem;margin:.9rem 0}
.douteux{border-color:#c9c9c9;background:#fafafa}
.nom{float:right;font-family:ui-monospace,monospace;font-size:.82rem;background:#2d5a86;color:#fff;
padding:.2rem .55rem;border-radius:5px}.douteux .nom{background:#777}
.num{font-weight:700;color:#555;font-size:.9rem}
.enonce{margin:.5rem 0;white-space:pre-wrap}.desc{color:#204a72;font-size:.92rem;margin-top:.5rem}
.intro{background:#f6f6f6;border-radius:9px;padding:.9rem 1.1rem}
code{background:#eee;padding:.1rem .3rem;border-radius:4px}</style>
<h1>Tableaux et tracés à fournir</h1>
<div class='intro'>Ces exercices sont <b>masqués</b>. Ce qui leur manque n'est pas le dessin
d'une figure mais une <b>mise en page</b> : un tableau à remplir, deux colonnes à relier,
une grille. Photographie-les comme les figures et dépose-les dans
<code>exercices/figures/</code>.</div>"""]
par = {}
for titre, num, nom, texte, desc in attente: par.setdefault(titre, []).append((num, nom, texte, desc))
for titre in sorted(par, key=lambda k: -len(par[k])):
    s.append(f"<h2>{html.escape(titre)} — {len(par[titre])}</h2>")
    for num, nom, texte, desc in sorted(par[titre]):
        s.append(f"<div class='ex'><span class='nom'>{nom}</span>"
                 f"<span class='num'>Exercice {num}</span>"
                 f"<div class='enonce'>{texte}</div>"
                 f"<div class='desc'><b>À fournir :</b> {html.escape(desc)}</div></div>")
if douteux:
    s.append("<h2>À ton jugement — figure présente, mais le tableau peut manquer</h2>")
    for titre, num, nom, texte in sorted(douteux):
        s.append(f"<div class='ex douteux'><span class='nom'>{nom}</span>"
                 f"<span class='num'>{html.escape(titre)} — exercice {num}</span>"
                 f"<div class='enonce'>{texte}</div>"
                 f"<div class='desc'>Cet exercice a déjà une figure, mais son énoncé parle "
                 f"d'un tableau. Vérifie si le tableau figure bien sur l'image.</div></div>")
s.append(f"<div class='intro'><b>{len(attente)} images à fournir</b>"
         + (f", et {len(douteux)} à vérifier." if douteux else ".") + "</div>")
open("apercu-tableaux.html", "w", encoding="utf-8").write("\n".join(s))
print(f"  {len(attente)} à fournir, {len(douteux)} à vérifier → apercu-tableaux.html")
for titre in sorted(par, key=lambda k: -len(par[k])):
    print(f"    {titre} — {', '.join(n for _, n, _, _ in sorted(par[titre]))}")
webbrowser.open("file://" + os.path.abspath("apercu-tableaux.html"))
