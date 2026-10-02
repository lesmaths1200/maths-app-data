#!/usr/bin/env python3
"""Génère un aperçu lisible des TAF blancs : énoncé puis corrigé.

Le JSON n'est pas relisible pour vérifier des mathématiques. Cette page HTML
affiche les formules via MathJax et s'imprime en PDF depuis le navigateur.
"""
import html
import json
import pathlib

RACINE = pathlib.Path(__file__).parent
SORTIE = RACINE / "apercu-taf-blancs.html"

ENTETE = """<!doctype html>
<meta charset="utf-8">
<title>TAF blancs — aperçu</title>
<script>window.MathJax={tex:{inlineMath:[['$','$']]}};</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
 body{font:16px/1.6 -apple-system,system-ui,sans-serif;max-width:46em;margin:2em auto;padding:0 1.5em;color:#1a1a1a}
 h1{font-size:1.7em;margin-bottom:.2em}
 h2{margin-top:2.4em;padding-top:.8em;border-top:3px solid #1836b2;color:#1836b2}
 h3{margin-top:1.8em;font-size:1.05em}
 .pts{float:right;font-weight:400;color:#777;font-size:.85em}
 .consigne{margin:.3em 0 .9em}
 .sous{margin:.5em 0 .5em 1.4em}
 .lib{font-weight:700;margin-right:.4em}
 .corrige{background:#f4f1fa;border-left:4px solid #a066cb;padding:.7em 1em;margin:.4em 0 .9em 1.4em;border-radius:0 6px 6px 0}
 .meta{background:#f5f5f5;padding:1em 1.2em;border-radius:8px;font-size:.92em}
 .meta li{margin:.2em 0}
 @media print{h2{page-break-before:always}}
</style>
"""


def bloc(texte):
    """Conserve les retours à la ligne du corrigé, qui séparent les étapes."""
    return "<br>".join(html.escape(l) if False else l for l in texte.split("\n"))


def main():
    donnees = json.loads((RACINE / "taf-blancs.json").read_text())
    meta = donnees["_metadata"]
    sortie = [ENTETE, "<h1>TAF blancs — aperçu</h1>"]

    sortie.append('<div class="meta"><b>Consignes</b><ul>')
    for c in meta["consignes"]:
        sortie.append(f"<li>{c}</li>")
    sortie.append(f'</ul><b>Durée</b> : {meta["dureeNormaleMinutes"]} min '
                  f'(ou {meta["dureeAmenageeMinutes"]} min aménagées)<br><br>'
                  f'<i>{meta["avertissementConstruction"]}</i></div>')

    for ep in donnees["epreuves"]:
        total = sum(q["points"] for q in ep["questions"])
        sortie.append(f'<h2>{ep["titre"]} <span class="pts">{total} points</span></h2>')
        for q in ep["questions"]:
            sortie.append(f'<h3>Question {q["numero"]} '
                          f'<span class="pts">{q["points"]} pts</span></h3>')
            sortie.append(f'<div class="consigne">{q["consigne"]}</div>')
            for s in q["sousQuestions"]:
                lib = f'<span class="lib">{s["libelle"]})</span>' if s["libelle"] else ""
                sortie.append(f'<div class="sous">{lib}{s["enonce"]}</div>')
                sortie.append(f'<div class="corrige">{bloc(s["reponse"])}</div>')

    SORTIE.write_text("\n".join(sortie))
    print(SORTIE)


if __name__ == "__main__":
    main()
