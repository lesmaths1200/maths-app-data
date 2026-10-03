#!/usr/bin/env python3
"""Aperçu HTML des EVACOM blancs, pour une relecture confortable des formules."""
import json, html, webbrowser, os

d = json.load(open("evacom-blancs.json"))
m = d["_metadata"]
s = ["""<!doctype html><meta charset="utf-8"><title>EVACOM blancs</title>
<script>window.MathJax={tex:{inlineMath:[['$','$']]}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
 body{font:16px/1.65 -apple-system,system-ui,sans-serif;max-width:760px;margin:2rem auto;padding:0 1rem;color:#1a1a1a}
 h1{font-size:1.6rem} h2{margin-top:2.5rem;border-top:3px solid #111;padding-top:1rem}
 .partie{background:#111;color:#fff;padding:.45rem .8rem;border-radius:7px;margin:1.8rem 0 .8rem;font-weight:600}
 .q{border:1px solid #ddd;border-radius:10px;padding:.9rem 1.1rem;margin:.9rem 0}
 .num{font-weight:700} .pts{float:right;color:#777;font-size:.85rem}
 .consigne{margin:.3rem 0 .7rem}
 .sq{margin:.55rem 0 .55rem 1rem} .lib{font-weight:700;margin-right:.35rem}
 .rep{background:#f4f7f4;border-left:3px solid #2d7a3e;padding:.5rem .8rem;margin:.35rem 0 0 1rem;white-space:pre-wrap;font-size:.94rem}
 .meta{background:#f6f6f6;border-radius:9px;padding:.8rem 1.1rem;font-size:.93rem}
</style>"""]
s.append("<h1>EVACOM blancs — relecture</h1><div class='meta'><b>Consignes</b><ul>")
for c in m["consignes"]: s.append(f"<li>{html.escape(c)}</li>")
s.append(f"</ul><b>Durée</b> : {m['dureeTotaleMinutes']} min, dont {m['dureePartie1Minutes']} min "
         f"pour la partie 1 — {m['dureeAmenageeMinutes']} min avec temps supplémentaire.</div>")

for e in d["epreuves"]:
    s.append(f"<h2>{html.escape(e['titre'])} — {e['totalPoints']} points</h2>")
    partie = None
    for q in e["questions"]:
        if q["partie"] != partie:
            partie = q["partie"]
            libelle = ("Partie 1 — sans calculatrice" if partie == 1 else "Partie 2 — calculatrice autorisée")
            pts = e["pointsPartie1"] if partie == 1 else e["pointsPartie2"]
            s.append(f"<div class='partie'>{libelle} · {pts} points</div>")
        s.append(f"<div class='q'><span class='pts'>{q['points']} pts</span>"
                 f"<span class='num'>Question {q['numero']}</span>"
                 f"<div class='consigne'>{q['consigne']}</div>")
        for sq in q["sousQuestions"]:
            lib = f"<span class='lib'>{sq['libelle']})</span>" if sq["libelle"] else ""
            s.append(f"<div class='sq'>{lib}{sq['enonce']}</div>")
            s.append(f"<div class='rep'>{sq['reponse']}</div>")
        s.append("</div>")

open("apercu-evacom-blancs.html", "w").write("\n".join(s))
print("aperçu écrit : apercu-evacom-blancs.html")
webbrowser.open("file://" + os.path.abspath("apercu-evacom-blancs.html"))
