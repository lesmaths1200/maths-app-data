# -*- coding: utf-8 -*-
"""Génère les dix EVACOM blancs de la section CT sur le squelette validé."""
import random
import complements
from fractions import Fraction as F

TRIPLETS = [
    (3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15),
    (9, 40, 41), (10, 24, 26), (11, 60, 61), (12, 16, 20), (12, 35, 37), (14, 48, 50),
    (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), (20, 48, 52),
    (21, 28, 35), (24, 32, 40), (24, 45, 51), (25, 60, 65), (27, 36, 45), (28, 45, 53),
    (30, 40, 50), (32, 60, 68), (33, 44, 55), (33, 56, 65), (36, 48, 60), (39, 52, 65),
    (40, 42, 58), (42, 56, 70), (45, 60, 75), (48, 55, 73),
]

def fr(n, d): return rf"\frac{{{n}}}{{{d}}}"

THEMES = {1: 'Nombres relatifs', 2: 'Fractions', 3: 'Fractions', 4: 'Solides', 5: 'Fractions', 6: 'Théorème de Pythagore', 7: 'Unités de mesure', 8: 'Théorème de Pythagore', 9: 'Théorème de Pythagore', 10: 'Proportionnalité', 11: 'Aires et volumes', 12: 'Aires et volumes', 13: 'Unités de mesure'}

def q(numero, points, partie, consigne, sous):
    return {"numero": numero, "points": points, "partie": partie,
            "theme": THEMES[numero], "consigne": consigne,
            "sousQuestions": [{"libelle": l, "enonce": e, "reponse": r} for l, e, r in sous]}

def engendrer(variante):
    r = random.Random(7000 + variante)

    # Q1 — nombres relatifs
    a1, b1 = r.randint(20, 60), r.randint(30, 80)
    a2, b2 = r.randint(20, 60), r.randint(5, 30)
    a3, b3 = r.randint(3, 9), r.randint(4, 9)
    b4 = r.choice([4, 6, 7, 8, 9]); a4 = b4 * r.randint(4, 11)
    q1 = q(1, 4, 1, "Calcule.", [
        ("a", rf"$(+{a1}) + (-{b1}) =$", rf"${a1-b1}$" "\n\n" +
         (rf"On retranche : ${b1} - {a1} = {b1-a1}$, et le plus grand nombre, ${b1}$, est négatif."
          if b1 > a1 else rf"On retranche : ${a1} - {b1} = {a1-b1}$, et le plus grand nombre, ${a1}$, est positif.")),
        ("b", rf"$(+{a2}) - (-{b2}) =$", rf"${a2+b2}$" "\n\n" rf"Soustraire un négatif revient à ajouter : ${a2} + {b2} = {a2+b2}$."),
        ("c", rf"$(-{a3}) \cdot (-{b3}) =$", rf"${a3*b3}$" "\n\n" r"Deux facteurs négatifs donnent un produit positif."),
        ("d", rf"$(-{a4}) : (+{b4}) =$", rf"${-(a4//b4)}$" "\n\n" r"Les signes sont différents, le quotient est négatif."),
    ])

    # Q2 — fractions, produit et quotient
    n1, d1 = [(8,15),(9,14),(10,21),(12,25),(14,15),(6,35),(15,22),(21,20),(16,27),(25,14)][(variante - 1) % 10]
    n2, d2 = r.choice([(5,12),(3,7),(7,8),(5,9),(9,10),(7,12)])
    p, qt = F(n1,d1)*F(n2,d2), F(n1,d1)/F(n2,d2)
    q2 = q(2, 4, 1, "Calcule et donne la réponse sous forme d'une fraction irréductible.", [
        ("a", rf"${fr(n1,d1)} \cdot {fr(n2,d2)} =$",
         rf"${fr(p.numerator,p.denominator)}$" "\n\n" rf"$\frac{{{n1} \cdot {n2}}}{{{d1} \cdot {d2}}} = \frac{{{n1*n2}}}{{{d1*d2}}} = {fr(p.numerator,p.denominator)}$."),
        ("b", rf"${fr(n1,d1)} : {fr(n2,d2)} =$",
         rf"${fr(qt.numerator,qt.denominator)}$" "\n\n" rf"Diviser, c'est multiplier par l'inverse : ${fr(n1,d1)} \cdot {fr(d2,n2)} = \frac{{{n1*d2}}}{{{d1*n2}}} = {fr(qt.numerator,qt.denominator)}$."),
    ])

    # Q3 — compléter des fractions
    dA = r.choice([8,10,12,15,16]); xa = r.randint(2, dA-3); ya = r.randint(1, dA-xa-1)
    na, nb = r.choice([(3,4),(2,3),(5,6),(3,5)]); mb = r.randint(2, 5)
    dC = r.choice([10,12,15,20]); dcs = dC // r.choice([d for d in (2,5) if dC % d == 0]); xc = r.randint(1, dcs-1)
    q3 = q(3, 3, 1, "Complète pour que chaque égalité soit vérifiée.", [
        ("a", rf"${fr(xa,dA)} + \frac{{\square}}{{{dA}}} = {fr(xa+ya,dA)}$",
         rf"${ya}$" "\n\n" rf"Les dénominateurs sont égaux : ${xa+ya} - {xa} = {ya}$."),
        ("b", rf"${fr(na,nb)} \cdot \frac{{\square}}{{{mb}}} = {fr(na*2, nb*mb)}$" if False else
              rf"${fr(na,nb)} \cdot \frac{{\square}}{{{mb}}} = \frac{{{na*2}}}{{{nb*mb}}}$",
         r"$2$" "\n\n" rf"$\frac{{{na} \cdot 2}}{{{nb} \cdot {mb}}} = \frac{{{na*2}}}{{{nb*mb}}}$."),
        ("c", rf"$\frac{{{xc * (dC//dcs) + 1}}}{{{dC}}} - \frac{{\square}}{{{dcs}}} = \frac{{1}}{{{dC}}}$",
         rf"${xc}$" "\n\n" rf"$\frac{{{xc}}}{{{dcs}}} = \frac{{{xc*(dC//dcs)}}}{{{dC}}}$, et $\frac{{{xc*(dC//dcs)+1}}}{{{dC}}} - \frac{{{xc*(dC//dcs)}}}{{{dC}}} = \frac{{1}}{{{dC}}}$."),
    ])

    # Q4 — solides (l'ordre des descriptions change d'une épreuve à l'autre)
    catalogue = [
        ("le cube", "Six faces carrées."),
        ("le pavé droit", "Six faces rectangulaires, huit sommets et douze arêtes."),
        ("le cylindre", "Deux bases circulaires identiques et parallèles, reliées par une surface courbe."),
        ("la pyramide à base carrée", "Une base carrée et quatre faces triangulaires qui se rejoignent en un sommet."),
        ("le cône", "Une base circulaire et une pointe, reliées par une surface courbe."),
        ("la boule", "Aucune face plane, aucun sommet, aucune arête."),
        ("le prisme à base triangulaire", "Deux bases triangulaires identiques et trois faces rectangulaires."),
        ("la pyramide à base triangulaire", "Quatre faces triangulaires, quatre sommets et six arêtes."),
    ]
    solides = r.sample(catalogue, 4)
    ordre = list(range(4)); r.shuffle(ordre)
    lettres = "abcd"
    liste = "  ·  ".join(f"{lettres[i]}) {solides[i][0]}" for i in range(4))
    descr = "\n".join(f"{j+1}. {solides[ordre[j]][1]}" for j in range(4))
    cle = "  ·  ".join(f"{lettres[i]}) {ordre.index(i)+1}" for i in range(4))
    q4 = q(4, 4, 1, "Associe chaque solide à sa description. Écris le numéro de la description en face du solide.", [
        ("", f"Solides : {liste}\n\nDescriptions :\n{descr}",
         f"{cle}\n\nLe cube est un pavé droit particulier : ses six faces sont des carrés."),
    ])

    # Q5 — fraction d'une fraction
    fn, fd = r.choice([(3,5),(2,3),(3,4),(4,5),(5,6)])
    gn, gd = r.choice([(1,4),(1,3),(2,5),(1,2)])
    part = F(fn,fd)*F(gn,gd)
    total = r.choice([600, 720, 840, 900, 1200])
    while (part*total).denominator != 1:
        total += 60
    objet, sous_objet = r.choice([("livres","romans"),("élèves","demi-pensionnaires"),("articles","soldés")])
    q5 = q(5, 3, 1, "Résous le problème.", [
        ("", rf"Une collection compte ${total}$ {objet}. Les ${fr(fn,fd)}$ sont des {sous_objet}. "
             rf"Parmi ces {sous_objet}, ${fr(gn,gd)}$ ont une particularité." "\n"
             rf"a) Quelle fraction de la collection cela représente-t-il ?" "\n"
             rf"b) Combien cela fait-il d'éléments ?",
         rf"a) ${fr(part.numerator,part.denominator)}$" "\n\n" rf"${fr(fn,fd)} \cdot {fr(gn,gd)} = {fr(part.numerator,part.denominator)}$." "\n\n"
         rf"b) ${part*total}$" "\n\n" rf"${fr(part.numerator,part.denominator)}$ de ${total}$ donne ${part*total}$."),
    ])

    # Q6 — Pythagore, vocabulaire et égalité
    listeSommets = [("A","B","C"), ("K","L","M"), ("P","Q","R"), ("D","E","F"),
                        ("E","F","G"), ("M","N","P"), ("R","S","T"), ("U","V","W"),
                        ("A","C","E"), ("B","D","F"), ("H","I","J"), ("L","M","N")]
    sommets = listeSommets[(variante - 1) % len(listeSommets)]
    X, Y, Z = sommets  # angle droit en Y, hypoténuse XZ
    q6 = q(6, 4, 1, "Le théorème de Pythagore.", [
        ("a", r.choice([
            "Complète : le théorème de Pythagore s'applique uniquement dans un triangle ______.",
            "Complète : dans un triangle rectangle, le côté opposé à l'angle droit s'appelle l'______.",
            "Complète : dans un triangle rectangle, les deux côtés de l'angle droit s'appellent les ______.",
            "Complète : l'hypoténuse est toujours le côté le plus ______ d'un triangle rectangle.",
         ]) if False else "Complète : le théorème de Pythagore s'applique uniquement dans un triangle ______.",
         "rectangle\n\nIl relie les deux cathètes à l'hypoténuse d'un triangle rectangle."),
        ("b", rf"Dans un triangle ${X}{Y}{Z}$ rectangle en ${Y}$, coche la seule égalité correcte." "\n"
              rf"1. ${X}{Y}^2 + {Y}{Z}^2 = {X}{Z}^2$" "\n"
              rf"2. ${X}{Y}^2 + {X}{Z}^2 = {Y}{Z}^2$" "\n"
              rf"3. ${X}{Z}^2 + {Y}{Z}^2 = {X}{Y}^2$",
         r"La n° 1." "\n\n" rf"L'angle droit est en ${Y}$, donc l'hypoténuse est le côté opposé $[{X}{Z}]$ : "
         rf"la somme des carrés des cathètes ${X}{Y}$ et ${Y}{Z}$ vaut ${X}{Z}^2$."),
    ])

    # Q7 — ordres de grandeur
    pool = [("La hauteur d'une porte d'appartement", "0,2 m  ·  2 m  ·  20 m", r"$2$ m", r"$0{,}2$ m ferait $20$ cm, et $20$ m la hauteur d'un immeuble."),
            ("La contenance d'une canette", "3 dl  ·  3 l  ·  3 hl", r"$3$ dl", r"$3$ dl $= 0{,}3$ litre, soit $300$ ml."),
            ("La masse d'une pomme", "15 g  ·  150 g  ·  1500 g", r"$150$ g", r"$1500$ g feraient $1{,}5$ kg, bien trop lourd."),
            ("La longueur d'un terrain de football", "10 m  ·  100 m  ·  1000 m", r"$100$ m", r"Un terrain réglementaire mesure entre $90$ et $120$ m."),
            ("La masse d'un vélo", "1,2 kg  ·  12 kg  ·  120 kg", r"$12$ kg", r"$1{,}2$ kg serait le poids d'une roue seule."),
            ("L'épaisseur d'une feuille de papier", "0,1 mm  ·  1 mm  ·  1 cm", r"$0{,}1$ mm", r"Cent feuilles empilées font environ $1$ cm."),
            ("La contenance d'une baignoire", "15 l  ·  150 l  ·  1500 l", r"$150$ l", r"$1500$ litres rempliraient une petite piscine.")]
    choisis = r.sample(pool, 3)
    q7 = q(7, 3, 1, "Pour chaque grandeur, coche l'estimation la plus réaliste.", [
        (l, f"{t} : {opts}", f"{rep}\n\n{just}") for l, (t, opts, rep, just) in zip("abc", choisis)
    ])

    # Q8 — hypoténuse
    ca, cb, hyp = r.choice(TRIPLETS)
    q8 = q(8, 2, 2, "Calcule.", [
        ("", rf"Un triangle rectangle a des cathètes de ${ca}$ cm et ${cb}$ cm. Calcule la longueur de son hypoténuse.",
         rf"${hyp}$ cm" "\n\n" rf"${ca}^2 + {cb}^2 = {ca*ca} + {cb*cb} = {hyp*hyp}$, et $\sqrt{{{hyp*hyp}}} = {hyp}$."),
    ])

    # Q9 — rectangle, diagonale et largeur
    ca2, cb2, hyp2 = r.choice([t for t in TRIPLETS if t != (ca, cb, hyp)])
    q9 = q(9, 4, 2, "Calcule.", [
        ("", rf"Un rectangle a une diagonale de ${hyp2}$ cm et une largeur de ${ca2}$ cm." "\n"
             rf"a) Calcule sa longueur." "\n" rf"b) Calcule son aire.",
         rf"a) ${cb2}$ cm" "\n\n" rf"${hyp2}^2 - {ca2}^2 = {hyp2*hyp2} - {ca2*ca2} = {cb2*cb2}$, et $\sqrt{{{cb2*cb2}}} = {cb2}$." "\n\n"
         rf"b) ${ca2*cb2}$ $\mathrm{{cm}}^2$" "\n\n" rf"${cb2} \cdot {ca2} = {ca2*cb2}$."),
    ])

    # Q10 — comparaison de vitesses
    v1 = r.choice([80, 90, 96, 100, 105, 110, 120])
    duree = r.choice([F(3,2), F(5,4), F(2), F(5,2), F(7,4)])
    d1 = int(v1 * duree)
    v2 = v1 + r.choice([-12, -8, -5, 5, 8, 12])
    d2 = v2 * 2
    heures = f"{int(duree)} h" if duree.denominator == 1 else f"{int(duree)} h {int((duree - int(duree)) * 60):02d}"
    gagnante = "rouge" if v1 > v2 else "verte"
    q10 = q(10, 4, 2, "Compare et justifie.", [
        ("", rf"Une voiture rouge parcourt ${d1}$ km en {heures}. Une voiture verte parcourt ${d2}$ km en $2$ h." "\n"
             rf"Quelle voiture roule le plus vite ? Justifie.",
         rf"La voiture {gagnante}." "\n\n"
         rf"Rouge : ${d1} : {str(duree).replace('/', '/')} = {v1}$ km/h. Verte : ${d2} : 2 = {v2}$ km/h." "\n"
         rf"La {gagnante} roule donc plus vite, à ${max(v1,v2)}$ km/h contre ${min(v1,v2)}$ km/h."),
    ])

    # Q11 — volume d'un cylindre
    import math
    rc, hc = r.randint(3, 9), r.randint(7, 20)
    vol = round(math.pi * rc * rc * hc, 1)
    q11 = q(11, 3, 2, "Calcule et arrondis au dixième.", [
        ("", rf"Calcule le volume d'un cylindre de rayon ${rc}$ cm et de hauteur ${hc}$ cm. Donne la réponse avec son unité.",
         rf"${str(vol).replace('.', '{,}')}$ $\mathrm{{cm}}^3$" "\n\n"
         rf"$V = \pi \cdot r^2 \cdot h = \pi \cdot {rc*rc} \cdot {hc} = {rc*rc*hc}\pi \approx {str(vol).replace('.', '{,}')}$ $\mathrm{{cm}}^3$."),
    ])

    # Q12 — choix du moule
    arete = r.randint(3, 6)
    dims = r.choice([(5,4,3),(6,3,2),(7,2,3),(4,4,2),(6,4,2)])
    va, vb = arete**3, dims[0]*dims[1]*dims[2]
    litres = r.choice([2, 3, 4, 5])
    cm3 = litres * 1000
    na, nb = cm3 // va, cm3 // vb
    meilleur = "A" if na > nb else "B"
    q12 = q(12, 5, 2, "Choisis et justifie.", [
        ("", rf"Un pâtissier dispose de deux moules." "\n"
             rf"Moule A : un cube d'arête ${arete}$ cm." "\n"
             rf"Moule B : un pavé droit de ${dims[0]}$ cm, ${dims[1]}$ cm et ${dims[2]}$ cm." "\n"
             rf"Il veut fabriquer le plus grand nombre de gâteaux avec ${litres}$ litres de pâte." "\n"
             rf"Quel moule doit-il choisir ? Justifie.",
         rf"Le moule {meilleur}." "\n\n"
         rf"Moule A : ${arete}^3 = {va}$ $\mathrm{{cm}}^3$. Moule B : ${dims[0]} \cdot {dims[1]} \cdot {dims[2]} = {vb}$ $\mathrm{{cm}}^3$." "\n"
         rf"${litres}$ litres $= {cm3}$ $\mathrm{{cm}}^3$." "\n"
         rf"Avec A : ${cm3} : {va}$ donne ${na}$ gâteaux. Avec B : ${cm3} : {vb}$ donne ${nb}$ gâteaux." "\n"
         rf"Le moule {meilleur} en permet donc davantage."),
    ])

    # Q13 — longueur de fil
    nb_perles, arete_p = r.randint(18, 32), r.choice([6, 8, 10, 12])
    libre = r.choice([10, 15, 20, 25])
    total_mm = nb_perles * arete_p + 2 * libre
    cm = F(total_mm, 10)
    aff = str(cm) if cm.denominator == 1 else str(float(cm)).replace('.', '{,}')
    q13 = q(13, 3, 2, "Résous le problème.", [
        ("", rf"Un bijoutier enfile ${nb_perles}$ perles cubiques de ${arete_p}$ mm d'arête sur un fil. "
             rf"Il laisse ${libre}$ mm de fil libre à chaque extrémité." "\n"
             rf"Quelle longueur de fil lui faut-il, en cm ?",
         rf"${aff}$ cm" "\n\n"
         rf"Perles : ${nb_perles} \cdot {arete_p} = {nb_perles*arete_p}$ mm. Fil libre : $2 \cdot {libre} = {2*libre}$ mm." "\n"
         rf"Total : ${nb_perles*arete_p} + {2*libre} = {total_mm}$ mm $= {aff}$ cm."),
    ])

    questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13]
    epreuve = {"id": f"evacom-ct-{variante}", "niveau": "CT",
               "titre": f"EVACOM blanc n° {variante} — section CT",
               "questions": questions}
    # Une question de plus, dont le thème tourne, pour couvrir les
    # absences relevées dans les sept dernières années d'épreuves.
    return complements.ajouter(epreuve, "CT", variante, r)
