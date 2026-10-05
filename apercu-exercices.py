#!/usr/bin/env python3
"""Aperçu HTML des fiches d'exercices, pour les relire formules rendues.

Lit le dépôt privé : le fichier produit contient donc du contenu non public.
Il est ignoré par git, et reste sur la machine.

    python3 apercu-exercices.py            → toutes les fiches
    python3 apercu-exercices.py 25 32      → seulement celles-ci
"""
import html, json, os, subprocess, sys, webbrowser

DEPOT = "lesmaths1200/lesmaths1200-prive"


def lire(chemin):
    sortie = subprocess.run(
        ["gh", "api", f"repos/{DEPOT}/contents/{chemin}", "--jq", ".content"],
        capture_output=True, text=True, check=True).stdout
    import base64
    return json.loads(base64.b64decode(sortie))


def titres_chapitres():
    titres = {}
    import csv
    with open("cours.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter=";"):
            titres[r["id"]] = r["titre"]
    return titres


def main(cles):
    exercices, corrections, titres = lire("exercices/exercices.json"), \
        lire("corrections/corrections.json"), titres_chapitres()
    if not cles:
        cles = sorted(exercices, key=int)

    s = ["""<!doctype html><meta charset="utf-8"><title>Exercices — Maths 1200</title>
<script>window.MathJax={tex:{inlineMath:[['$','$']]}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
 body{font:16px/1.65 -apple-system,system-ui,sans-serif;max-width:820px;margin:2rem auto;
      padding:0 1rem;color:#1a1a1a}
 h1{font-size:1.5rem} h2{margin-top:2.6rem;border-top:3px solid #111;padding-top:.9rem}
 .ex{border:1px solid #ddd;border-radius:10px;padding:.9rem 1.1rem;margin:.9rem 0}
 .num{font-weight:700;color:#555;font-size:.9rem}
 .masque{background:#fff6f0;border-color:#f0c9a8}
 .etiquette{float:right;font-size:.75rem;color:#b35c00;font-weight:600}
 .enonce{margin:.4rem 0 .7rem;white-space:pre-wrap}
 .corr{background:#f4f7f4;border-left:3px solid #2d7a3e;padding:.55rem .85rem;
       white-space:pre-wrap;font-size:.94rem}
 .sans{background:#fdf0f0;border-left-color:#b33;padding:.55rem .85rem;font-size:.9rem}
 .resume{background:#f6f6f6;border-radius:9px;padding:.8rem 1.1rem;font-size:.93rem}
</style>
<h1>Exercices — relecture</h1>"""]

    total = masques = 0
    for cle in cles:
        fiche = exercices.get(str(cle))
        if not fiche:
            continue
        corr = {c["numero"]: c["texte"]
                for c in corrections.get(str(cle), {}).get("corrections", [])}
        titre = titres.get(str(cle), fiche.get("titre", f"Fiche {cle}"))
        visibles = sum(1 for e in fiche["exercices"]
                       if "[Figure" not in e["enonce"] and "[Tableau" not in e["enonce"])
        s.append(f"<h2>{html.escape(titre)}</h2>")
        s.append(f"<div class='resume'>{len(fiche['exercices'])} exercices, "
                 f"dont <b>{visibles} visibles</b> dans l'app. Les autres, sur fond orangé, "
                 f"sont masqués parce qu'ils renvoient à une figure absente.</div>")
        for e in fiche["exercices"]:
            total += 1
            cache = "[Figure" in e["enonce"] or "[Tableau" in e["enonce"]
            masques += cache
            s.append(f"<div class='ex{' masque' if cache else ''}'>")
            if cache:
                s.append("<span class='etiquette'>masqué dans l'app</span>")
            s.append(f"<span class='num'>Exercice {e['numero']}</span>")
            s.append(f"<div class='enonce'>{e['enonce']}</div>")
            texte = corr.get(e["numero"])
            s.append(f"<div class='corr'>{texte}</div>" if texte
                     else "<div class='corr sans'>Aucune correction pour cet exercice.</div>")
            s.append("</div>")

    s.append(f"<p class='resume'>{total} exercices au total, {masques} masqués.</p>")
    sortie = "apercu-exercices.html"
    with open(sortie, "w", encoding="utf-8") as f:
        f.write("\n".join(s))
    print(f"  {total} exercices, {masques} masqués → {sortie}")
    webbrowser.open("file://" + os.path.abspath(sortie))


if __name__ == "__main__":
    main(sys.argv[1:])
