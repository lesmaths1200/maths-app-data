#!/usr/bin/env python3
"""Compare, avant et après, les énoncés dont le tableau devient du texte.

Le fichier produit contient du contenu privé : il est ignoré par git.
"""
import base64, html, json, os, subprocess, sys, webbrowser

DEPOT = "lesmaths1200/lesmaths1200-prive"
sys.path.insert(0, "/tmp/conv")
from conversions import CONVERSIONS


def lire(chemin):
    sortie = subprocess.run(
        ["gh", "api", f"repos/{DEPOT}/contents/{chemin}", "--jq", ".content"],
        capture_output=True, text=True, check=True).stdout
    return json.loads(base64.b64decode(sortie))


def titres():
    import csv
    with open("cours.csv", encoding="utf-8") as f:
        return {r["id"]: r["titre"] for r in csv.DictReader(f, delimiter=";")}


ex, corr, noms = lire("exercices/exercices.json"), lire("corrections/corrections.json"), titres()

s = ["""<!doctype html><meta charset="utf-8"><title>Conversions de tableaux</title>
<script>window.MathJax={tex:{inlineMath:[['$','$']]}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
 body{font:16px/1.6 -apple-system,system-ui,sans-serif;max-width:1100px;margin:2rem auto;
      padding:0 1rem;color:#1a1a1a}
 h1{font-size:1.5rem} h2{font-size:1.05rem;margin:2.4rem 0 .6rem;
    border-top:2px solid #111;padding-top:.8rem}
 .paire{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
 .col{border-radius:10px;padding:.85rem 1rem;white-space:pre-wrap}
 .avant{background:#fdf1e7;border:1px solid #e9c39b}
 .apres{background:#eef6ef;border:1px solid #a9ceb0}
 .etiquette{font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase;
            display:block;margin-bottom:.5rem}
 .avant .etiquette{color:#9a5a12} .apres .etiquette{color:#2d7a3e}
 .corr{background:#f6f6f6;border-left:3px solid #999;padding:.5rem .85rem;margin-top:.6rem;
       white-space:pre-wrap;font-size:.93rem}
 .intro{background:#f6f6f6;border-radius:9px;padding:.9rem 1.1rem}
 @media (max-width:800px){.paire{grid-template-columns:1fr}}
</style>
<h1>Conversions de tableaux — avant / après</h1>
<div class='intro'>À gauche, l'énoncé tel qu'il est aujourd'hui : l'app le masque, car il
renvoie à un tableau qu'elle ne sait pas dessiner. À droite, la version proposée, qui dit le
même tableau en toutes lettres. <b>Les données sont identiques</b> ; seule la présentation
change. La correction existante est rappelée dessous, pour vérifier qu'elle reste valable.</div>"""]

for (cle, numero), nouveau in CONVERSIONS.items():
    ancien = next(e["enonce"] for e in ex[cle]["exercices"] if e["numero"] == numero)
    texte = next((c["texte"] for c in corr[cle]["corrections"] if c["numero"] == numero), None)
    s.append(f"<h2>{html.escape(noms.get(cle, cle))} — exercice {numero}</h2>")
    s.append("<div class='paire'>")
    s.append(f"<div class='col avant'><span class='etiquette'>Aujourd'hui · masqué</span>{ancien}</div>")
    s.append(f"<div class='col apres'><span class='etiquette'>Proposé · visible</span>{nouveau}</div>")
    s.append("</div>")
    s.append(f"<div class='corr'><b>Correction existante :</b>\n{texte}</div>" if texte
             else "<div class='corr'><b>Aucune correction pour cet exercice.</b></div>")

s.append(f"<p class='intro'>{len(CONVERSIONS)} conversions proposées.</p>")
sortie = "apercu-conversions.html"
with open(sortie, "w", encoding="utf-8") as f:
    f.write("\n".join(s))
print(f"  {len(CONVERSIONS)} conversions → {sortie}")
webbrowser.open("file://" + os.path.abspath(sortie))
