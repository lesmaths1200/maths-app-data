# -*- coding: utf-8 -*-
"""Génère les dix EVACOM blancs de la section LC."""
import random
from fractions import Fraction as F

TRIPLETS = [(3,4,5),(6,8,10),(9,12,15),(5,12,13),(8,15,17),(7,24,25),(20,21,29),
            (9,40,41),(12,35,37),(10,24,26),(15,20,25),(24,32,40),(16,30,34),(14,48,50)]
CARRES = [4,9,16,25,36,49,64,81,100,121,144]

def fr(n, d): return rf"\frac{{{n}}}{{{d}}}"
def frac(x): return fr(x.numerator, x.denominator) if x.denominator != 1 else str(x.numerator)

def q(numero, points, partie, consigne, sous):
    return {"numero": numero, "points": points, "partie": partie, "consigne": consigne,
            "sousQuestions": [{"libelle": l, "enonce": e, "reponse": r} for l, e, r in sous]}

def engendrer(variante):
    r = random.Random(8000 + variante)

    # Q1 — fractions et racine
    f1 = (r.choice([5,7,11,13]), r.choice([6,8,9,12]))
    f2 = (r.choice([3,5,7]), r.choice([4,8,10,16]))
    g1 = r.choice([(14,9),(15,8),(21,10),(22,15)])
    g2 = r.choice([(7,6),(5,4),(7,5),(11,6)])
    h1 = r.choice([(15,8),(12,25),(20,9),(18,35)])
    h2 = r.choice([(12,25),(5,6),(14,15),(21,8)])
    car = r.choice(CARRES)
    a, b = F(*f1)-F(*f2), F(*g1)/F(*g2)
    c = F(*h1)*F(*h2)
    q1 = q(1, 6, 1, "Calcule et donne la réponse sous forme d'un entier ou d'une fraction irréductible.", [
        ("a", rf"${fr(*f1)} - {fr(*f2)} =$", rf"${frac(a)}$" "\n\n" rf"Au dénominateur commun : ${frac(a)}$."),
        ("b", rf"${fr(*g1)} : {fr(*g2)} =$", rf"${frac(b)}$" "\n\n" rf"${fr(*g1)} \cdot {fr(g2[1],g2[0])} = {frac(b)}$."),
        ("c", rf"${fr(*h1)} \cdot {fr(*h2)} =$", rf"${frac(c)}$" "\n\n" rf"$\frac{{{h1[0]*h2[0]}}}{{{h1[1]*h2[1]}}} = {frac(c)}$."),
        ("d", rf"${car} : \sqrt{{{car}}} =$", rf"${int(car**0.5)}$" "\n\n" rf"$\sqrt{{{car}}} = {int(car**0.5)}$, et ${car} : {int(car**0.5)} = {int(car**0.5)}$."),
    ])

    # Q2 — compléter
    dd = r.choice([8, 12, 16]); cible = r.randint(2, 3)
    t1, t2 = F(r.randint(1, dd-1), dd), F(r.randint(1, dd-1), dd)
    manque = F(cible) - t1 - t2
    while manque <= 0:
        cible += 1; manque = F(cible) - t1 - t2
    num_manque = manque * dd
    rac = r.choice(CARRES); dec = r.randint(2, 9)
    e1, e2 = r.choice([(10,15),(12,18),(14,21),(8,12)]); mult = r.choice([2,3,4])
    q2 = q(2, 4, 1, "Complète afin que chaque égalité soit vérifiée.", [
        ("a", rf"${frac(t1)} + {frac(t2)} + \frac{{\square}}{{{dd}}} = {cible}$",
         rf"${num_manque}$" "\n\n" rf"${frac(t1)} + {frac(t2)} = {frac(t1+t2)}$, et ${cible} = {fr(cible*dd, dd)}$ : il manque $\frac{{{num_manque}}}{{{dd}}}$."),
        ("b", rf"$\sqrt{{\square}} + {dec} = {int(rac**0.5) + dec}$",
         rf"${rac}$" "\n\n" rf"$\sqrt{{\square}} = {int(rac**0.5)}$, donc $\square = {rac}$."),
        ("c", rf"$\frac{{\square}}{{{F(e1,e2).denominator * mult}}} = {fr(*e1_e2) if False else fr(e1, e2)}$",
         rf"${F(e1,e2).numerator * mult}$" "\n\n" rf"${fr(e1,e2)} = {frac(F(e1,e2))}$, qu'on amplifie par ${mult}$."),
    ])

    # Q3 — partage avec prélèvement
    nb_parts = r.choice([3, 4, 5]); denom = r.choice([3, 4, 5])
    part = r.choice([8000, 12000, 15000, 9000, 18000])
    reste = nb_parts * part
    total = F(reste * denom, denom - 1)
    while total.denominator != 1:
        part += 1000; reste = nb_parts * part; total = F(reste * denom, denom - 1)
    mot = {3: "le tiers", 4: "le quart", 5: "le cinquième"}[denom]
    heritiers = {3: "Trois frères", 4: "Quatre sœurs", 5: "Cinq cousins"}[nb_parts]
    q3 = q(3, 2, 1, "Résous le problème.", [
        ("", rf"{heritiers} se partagent un héritage. L'État prélève d'abord {mot} du total. "
             rf"Ils se partagent équitablement ce qui reste et reçoivent CHF $\,{part}$ chacun." "\n"
             rf"À combien s'élevait l'héritage au départ ?",
         rf"CHF $\,{int(total)}$" "\n\n"
         rf"Ensemble ils reçoivent ${nb_parts} \cdot {part} = {reste}$ CHF, soit les ${fr(denom-1, denom)}$ de l'héritage." "\n"
         rf"Un ${denom}^e$ vaut donc ${reste} : {denom-1} = {reste//(denom-1)}$, et le total ${reste//(denom-1)} \cdot {denom} = {int(total)}$."),
    ])

    # Q4 — compléter des égalités littérales
    k1, k2 = r.randint(3, 9), r.randint(2, 6)
    cst = r.randint(5, 15)
    p1, p2 = r.randint(2, 6), r.randint(3, 8)
    q4 = q(4, 4, 1, "Complète afin que chaque égalité soit toujours vraie.", [
        ("a", rf"${k1}x + {cst} - (\square) = {k1-k2}x$",
         rf"${k2}x + {cst}$" "\n\n" rf"${k1}x + {cst} - ({k2}x + {cst}) = {k1-k2}x$."),
        ("b", rf"$(x + {p1})(x + \square) = x^2 + \square\,x + {p1*p2}$",
         rf"${p2}$ puis ${p1+p2}$" "\n\n" rf"$(x+{p1})(x+{p2}) = x^2 + {p2}x + {p1}x + {p1*p2} = x^2 + {p1+p2}x + {p1*p2}$."),
    ])

    # Q5 — développer avec identité remarquable
    m, n = r.randint(2, 6), r.randint(2, 9)
    dec2 = r.randint(2, 9)
    q5 = q(5, 2, 1, "Développe, puis donne la réponse sous forme réduite.", [
        ("", rf"$(x - {dec2}) + ({m}x + {n})({m}x - {n}) =$",
         rf"${m*m}x^2 + x - {dec2 + n*n}$" "\n\n"
         rf"$({m}x+{n})({m}x-{n}) = {m*m}x^2 - {n*n}$ (identité remarquable)." "\n"
         rf"Donc $x - {dec2} + {m*m}x^2 - {n*n} = {m*m}x^2 + x - {dec2+n*n}$."),
    ])

    # Q6 — aire par polynôme
    coef, cst6 = r.randint(2, 4), r.randint(3, 9)
    q6 = q(6, 3, 1, "Exprime l'aire à l'aide d'un polynôme réduit.", [
        ("", rf"Un grand rectangle mesure $({coef}x + {cst6})$ de long et $x$ de large. "
             rf"On y découpe un carré de côté $x$, que l'on retire." "\n"
             rf"Exprime l'aire de la surface restante à l'aide d'un polynôme réduit.",
         rf"${coef-1}x^2 + {cst6}x$" "\n\n"
         rf"Rectangle : $x({coef}x + {cst6}) = {coef}x^2 + {cst6}x$." "\n"
         rf"Carré : $x^2$." "\n"
         rf"Différence : ${coef}x^2 + {cst6}x - x^2 = {coef-1}x^2 + {cst6}x$."),
    ])

    # Q7 — problème des billes
    don = r.randint(2, 6)
    # l + don = t - don  →  t = l + 2*don ;  t + don = 2(l - don)  →  l = 4*don + ... 
    # l + 2don + don = 2l - 2don  →  l = 5*don
    l_, t_ = 5*don, 7*don
    prenoms = r.choice([("Léa","Tom"),("Nora","Sami"),("Elsa","Hugo"),("Maya","Rayan")])
    P1, P2 = prenoms
    q7 = q(7, 2, 1, "Résous le problème.", [
        ("", rf"{P1} et {P2} possèdent des billes. {P1} dit à {P2} : « Si tu me donnais ${don}$ billes, "
             rf"nous en aurions autant l'un que l'autre. »" "\n"
             rf"{P2} répond : « Et si tu m'en donnais ${don}$, j'en aurais le double de toi. »" "\n"
             rf"Combien de billes chacun possède-t-il ?",
         rf"{P1} en a ${l_}$, {P2} en a ${t_}$." "\n\n"
         rf"Soit $a$ les billes de {P1} et $b$ celles de {P2}." "\n"
         rf"Première phrase : $a + {don} = b - {don}$, donc $b = a + {2*don}$." "\n"
         rf"Seconde phrase : $b + {don} = 2(a - {don})$." "\n"
         rf"En substituant : $a + {3*don} = 2a - {2*don}$, donc $a = {l_}$ et $b = {t_}$." "\n"
         rf"Vérification : ${l_} + {don} = {l_+don}$ et ${t_} - {don} = {t_-don}$ ✓."),
    ])

    q8 = q(8, 2, 2, "Complète avec les mots qui conviennent.", [
        ("", "Mots proposés : hypoténuse  ·  cathètes  ·  rectangle  ·  isocèle  ·  réciproque\n\n"
             "Si le carré du plus grand côté d'un triangle est égal à la somme des carrés des deux autres, "
             "alors ce triangle est ______ . C'est la ______ du théorème de Pythagore.",
         "rectangle, puis réciproque\n\n"
         "La réciproque permet de démontrer qu'un triangle est rectangle à partir de ses seules longueurs."),
    ])

    # Q9 — substitution
    va, vc = r.randint(2, 8), -r.randint(2, 7)
    vb = F(r.randint(3, 15), 2)
    ka, kb = r.randint(2, 4), r.randint(2, 4)
    val = ka*va + kb*vb - vc
    vb_aff = str(vb).replace("/2", "") if vb.denominator == 1 else str(float(vb)).replace(".", "{,}")
    q9 = q(9, 2, 2, "Substitue puis calcule.", [
        ("", rf"Substitue $a = {va}$, $b = {vb_aff}$ et $c = {vc}$ dans l'expression ${ka}a + {kb}b - c$, puis calcule sa valeur.",
         rf"${frac(F(val))}$" "\n\n" rf"${ka} \cdot {va} + {kb} \cdot {vb_aff} - ({vc}) = {ka*va} + {frac(kb*vb)} + {-vc} = {frac(F(val))}$."),
    ])

    # Q10 — périmètres égaux
    dec10, cote = r.randint(1, 5), r.randint(4, 9)
    # 2(x+dec) + 2*cote = 6x  →  2x + 2dec + 2cote = 6x  →  x = (2dec+2cote)/4
    x10 = F(2*dec10 + 2*cote, 4)
    while x10.denominator != 1:
        cote += 1; x10 = F(2*dec10 + 2*cote, 4)
    q10 = q(10, 4, 2, "Trouve la valeur de x.", [
        ("", rf"Un rectangle a pour dimensions $(x + {dec10})$ et ${cote}$. "
             rf"Un triangle équilatéral a un côté de $2x$." "\n"
             rf"Quelle doit être la valeur de $x$ pour que les deux figures aient le même périmètre ?",
         rf"$x = {int(x10)}$" "\n\n"
         rf"Périmètre du rectangle : $2(x + {dec10}) + 2 \cdot {cote} = 2x + {2*dec10+2*cote}$." "\n"
         rf"Périmètre du triangle : $3 \cdot 2x = 6x$." "\n"
         rf"$2x + {2*dec10+2*cote} = 6x$, donc $4x = {2*dec10+2*cote}$ et $x = {int(x10)}$." "\n"
         rf"Vérification : rectangle ${2*(int(x10)+dec10) + 2*cote}$ ; triangle ${6*int(x10)}$ ✓."),
    ])

    # Q11 / Q12 — réciproque de Pythagore
    t11 = r.choice(TRIPLETS); t12 = r.choice([t for t in TRIPLETS if t != t11])
    q11 = q(11, 2, 2, "Justifie ta réponse.", [
        ("", rf"Une étagère est fixée contre un mur vertical. Elle avance de ${t11[0]}$ cm, "
             rf"son support descend de ${t11[1]}$ cm le long du mur, et la barre oblique qui relie "
             rf"les deux extrémités mesure ${t11[2]}$ cm." "\n"
             rf"L'étagère est-elle bien perpendiculaire au mur ? Justifie.",
         rf"Oui." "\n\n"
         rf"${t11[0]}^2 + {t11[1]}^2 = {t11[0]**2} + {t11[1]**2} = {t11[2]**2}$ et ${t11[2]}^2 = {t11[2]**2}$." "\n"
         rf"L'égalité de Pythagore est vérifiée : par la réciproque, le triangle est rectangle, "
         rf"donc l'étagère est perpendiculaire au mur."),
    ])
    S = r.choice([("A","B","C"),("D","E","F"),("K","L","M"),("P","Q","R")])
    q12 = q(12, 3, 2, "Justifie ta réponse.", [
        ("", rf"Un triangle ${S[0]}{S[1]}{S[2]}$ a pour côtés ${S[0]}{S[1]} = {t12[0]}$ cm, "
             rf"${S[1]}{S[2]} = {t12[1]}$ cm et ${S[0]}{S[2]} = {t12[2]}$ cm." "\n"
             rf"Ce triangle est-il rectangle ? Si oui, en quel sommet ?",
         rf"Oui, rectangle en ${S[1]}$." "\n\n"
         rf"Le plus grand côté est ${S[0]}{S[2]} = {t12[2]}$." "\n"
         rf"${t12[0]}^2 + {t12[1]}^2 = {t12[0]**2} + {t12[1]**2} = {t12[2]**2}$ et ${t12[2]}^2 = {t12[2]**2}$." "\n"
         rf"L'égalité est vérifiée, donc l'angle droit est opposé à $[{S[0]}{S[2]}]$, c'est-à-dire en ${S[1]}$."),
    ])

    # Q13 — losange
    D13 = r.choice([10, 12, 14, 16, 18, 20]); d13 = r.choice([6, 8, 9, 12, 15])
    aire13 = F(D13 * d13, 2)
    aff_aire = str(aire13) if aire13.denominator == 1 else str(float(aire13)).replace(".", "{,}")
    q13 = q(13, 3, 2, "Calcule.", [
        ("", rf"Un losange a une aire de ${aff_aire}$ $\mathrm{{cm}}^2$ et sa grande diagonale mesure ${D13}$ cm." "\n"
             rf"Calcule la longueur de sa petite diagonale.",
         rf"${d13}$ cm" "\n\n"
         rf"L'aire d'un losange vaut $\frac{{D \cdot d}}{{2}}$." "\n"
         rf"$\frac{{{D13} \cdot d}}{{2}} = {aff_aire}$, donc ${F(D13,2) if F(D13,2).denominator==1 else D13}d = {aff_aire if F(D13,2).denominator==1 else 2*aire13}$ et $d = {d13}$."),
    ])

    # Q14 — investissement
    perte = r.choice([3, 4, 5])          # perd 1/perte
    facteur = r.choice([3, 4, 5, 6])
    depart = r.choice([600, 900, 1200, 1500, 1800])
    reste_f = F(perte-1, perte) * depart * facteur
    while reste_f.denominator != 1:
        depart += 300; reste_f = F(perte-1, perte) * depart * facteur
    mot_perte = {3: "le tiers", 4: "le quart", 5: "le cinquième"}[perte]
    mot_fact = {3: "triple", 4: "quadruple", 5: "quintuple", 6: "sextuple"}[facteur]
    prenom = r.choice(["Sarah", "Nadia", "Chloé", "Yanis", "Ilyas"])
    q14 = q(14, 4, 2, "Résous le problème.", [
        ("", rf"{prenom} investit une somme dans un projet. Le premier mois, {'elle' if prenom[-1]=='a' or prenom in ('Chloé',) else 'il'} perd {mot_perte} de son "
             rf"investissement. Le deuxième mois, {mot_fact} ce qui reste. "
             rf"Le total atteint alors CHF $\,{int(reste_f)}$." "\n"
             rf"Combien avait-{'elle' if prenom[-1]=='a' or prenom in ('Chloé',) else 'il'} investi au départ ?",
         rf"CHF $\,{depart}$" "\n\n"
         rf"Soit $x$ l'investissement de départ." "\n"
         rf"Après le premier mois, il reste ${fr(perte-1, perte)}x$." "\n"
         rf"Après le deuxième : ${facteur} \cdot {fr(perte-1,perte)}x = {fr(facteur*(perte-1), perte)}x = {int(reste_f)}$." "\n"
         rf"Donc $x = {int(reste_f)} \cdot {fr(perte, facteur*(perte-1))} = {depart}$."),
    ])

    questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14]
    return {"id": f"evacom-lc-{variante}", "niveau": "LC",
            "titre": f"EVACOM blanc n° {variante} — section LC", "questions": questions}
