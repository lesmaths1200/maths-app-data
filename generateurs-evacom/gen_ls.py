# -*- coding: utf-8 -*-
"""Génère les dix EVACOM blancs de la section LS."""
import random, math
from fractions import Fraction as F
import complements

TRIPLETS = [
    (3, 4, 5), (5, 12, 13), (6, 8, 10), (7, 24, 25), (8, 15, 17), (9, 12, 15),
    (9, 40, 41), (10, 24, 26), (11, 60, 61), (12, 16, 20), (12, 35, 37), (14, 48, 50),
    (15, 20, 25), (15, 36, 39), (16, 30, 34), (18, 24, 30), (20, 21, 29), (20, 48, 52),
    (21, 28, 35), (24, 32, 40), (24, 45, 51), (25, 60, 65), (27, 36, 45), (28, 45, 53),
    (30, 40, 50), (32, 60, 68), (33, 44, 55), (33, 56, 65), (36, 48, 60), (39, 52, 65),
    (40, 42, 58), (42, 56, 70), (45, 60, 75), (48, 55, 73),
]
CARRES = [4,9,16,25,36,49,64,81,100,121,144]

def fr(n, d): return rf"\frac{{{n}}}{{{d}}}"
def coef(k):
    """« 1x » s'écrit « x », « -1x » s'écrit « -x »."""
    return "" if k == 1 else ("-" if k == -1 else str(k))
def frac(x): return fr(x.numerator, x.denominator) if x.denominator != 1 else str(x.numerator)
def virg(x, n):
    return f"{x:.{n}f}".replace(".", "{,}")

THEMES = {1: 'Racines carrées', 2: 'Racines carrées', 3: 'Racines carrées', 4: 'Calcul littéral', 5: 'Calcul littéral', 6: 'Aires et volumes', 7: 'Calcul littéral', 8: 'Calcul littéral', 9: 'Équations', 10: 'Solides', 11: 'Aires et volumes', 12: 'Aires et volumes', 13: 'Théorème de Pythagore'}

def q(numero, points, partie, consigne, sous):
    return {"numero": numero, "points": points, "partie": partie,
            "theme": THEMES[numero], "consigne": consigne,
            "sousQuestions": [{"libelle": l, "enonce": e, "reponse": r} for l, e, r in sous]}

def engendrer(variante):
    r = random.Random(9000 + variante)

    # Q1 — racines et fractions
    k = r.choice([2, 3, 5]); m = r.choice([2, 3, 4, 5])
    prod = k * m * m * k  # √(k·m²k) → on prend √(a)·√(b) avec a·b carré parfait
    a1, b1 = k, k * (m*m)   # √k · √(k m²) = k·m
    d1 = r.choice([3, 5, 7]); mult = r.choice([4, 9, 16])
    rac = r.choice([2, 3, 5, 6, 7])
    ent = r.randint(2, 6)
    f1 = r.choice([(7,12),(5,18),(11,15),(7,10),(13,20)])
    f2 = r.choice([(5,18),(7,12),(4,15),(3,10),(7,20)])
    somme = F(*f1) + F(*f2)
    q1 = q(1, 5, 1, "Calcule et donne les réponses sous la forme d'une fraction irréductible ou d'un entier.", [
        ("a", rf"$\sqrt{{{a1}}} \cdot \sqrt{{{b1}}} =$", rf"${k*m}$" "\n\n"
         rf"$\sqrt{{{a1}}} \cdot \sqrt{{{b1}}} = \sqrt{{{a1*b1}}} = {k*m}$."),
        ("b", rf"$\frac{{\sqrt{{{d1*mult}}}}}{{\sqrt{{{d1}}}}} =$", rf"${int(math.isqrt(mult))}$" "\n\n"
         rf"$\sqrt{{\frac{{{d1*mult}}}{{{d1}}}}} = \sqrt{{{mult}}} = {int(math.isqrt(mult))}$."),
        ("c", rf"$(\sqrt{{{rac}}} + {ent})(\sqrt{{{rac}}} - {ent}) =$", rf"${rac - ent*ent}$" "\n\n"
         rf"Identité remarquable : $(\sqrt{{{rac}}})^2 - {ent}^2 = {rac} - {ent*ent} = {rac-ent*ent}$."),
        ("d", rf"${fr(*f1)} + {fr(*f2)} =$", rf"${frac(somme)}$" "\n\n"
         rf"Au dénominateur commun, la somme vaut ${frac(somme)}$."),
    ])

    # Q2 — écrire sous la forme a√b
    base = r.choice([2, 3, 5, 6, 7])
    c1, c2, c3 = r.sample([2, 3, 4, 5, 6, 7], 3)
    q2 = q(2, 3, 1, rf"Écris sous la forme $a\sqrt{{b}}$, où $a$ est un entier et $b$ le plus petit possible.", [
        ("a", rf"$\sqrt{{{c1*c1*base}}} =$", rf"${c1}\sqrt{{{base}}}$" "\n\n"
         rf"${c1*c1*base} = {c1*c1} \cdot {base}$, donc $\sqrt{{{c1*c1*base}}} = \sqrt{{{c1*c1}}}\sqrt{{{base}}} = {c1}\sqrt{{{base}}}$."),
        ("b", rf"$\sqrt{{{c2*c2*base}}} =$", rf"${c2}\sqrt{{{base}}}$" "\n\n"
         rf"${c2*c2*base} = {c2*c2} \cdot {base}$, donc $\sqrt{{{c2*c2*base}}} = {c2}\sqrt{{{base}}}$."),
        ("c", rf"$\sqrt{{{c3*c3} \cdot {base}}} =$", rf"${c3}\sqrt{{{base}}}$" "\n\n"
         rf"${c3*c3} \cdot {base} = {c3*c3*base}$, donc $\sqrt{{{c3*c3*base}}} = {c3}\sqrt{{{base}}}$."),
    ])

    # Q3 — QCM
    n3 = r.choice([10, 20, 30, 40, 50, 60, 70, 90])
    bas = math.isqrt(n3); haut = bas + 1
    while bas*bas == n3:
        n3 += 1; bas = math.isqrt(n3); haut = bas + 1
    neg = r.choice([2, 3, 4, 5]); expo = r.choice([2, 4])
    car3 = r.choice([4, 9, 16, 25, 36, 49])
    q3 = q(3, 3, 1, "Pour chaque item, coche la seule bonne réponse.", [
        ("a", rf"$\sqrt{{{n3}}}$ est compris entre :" "\n"
              rf"${bas-1}$ et ${bas}$  ·  ${bas}$ et ${haut}$  ·  ${haut}$ et ${haut+1}$",
         rf"Entre ${bas}$ et ${haut}$" "\n\n" rf"${bas}^2 = {bas*bas}$ et ${haut}^2 = {haut*haut}$, or ${bas*bas} < {n3} < {haut*haut}$."),
        ("b", rf"$(-{neg})^{expo}$ vaut :" "\n" rf"$-{neg**expo}$  ·  ${neg**expo}$  ·  $-{neg*expo}$",
         rf"${neg**expo}$" "\n\n" r"L'exposant est pair, donc le résultat est positif."),
        ("c", rf"$x^2 - {car3}$ se factorise en :" "\n"
              rf"$(x-{int(math.isqrt(car3))})^2$  ·  $(x+{int(math.isqrt(car3))})(x-{int(math.isqrt(car3))})$  ·  $(x+{car3})(x-1)$",
         rf"$(x+{int(math.isqrt(car3))})(x-{int(math.isqrt(car3))})$" "\n\n" r"C'est la différence de deux carrés."),
    ])

    # Q4 — développer
    u, v = r.randint(2, 5), r.randint(2, 7)
    w, z = r.randint(2, 6), r.randint(2, 5)
    q4 = q(4, 3, 1, "Développe et réduis.", [
        ("a", rf"$({u}x - {v})^2 =$", rf"${u*u}x^2 - {2*u*v}x + {v*v}$" "\n\n"
         rf"$({u}x)^2 - 2 \cdot {u}x \cdot {v} + {v}^2$."),
        ("b", rf"$(x + {w})({z}x - 1) - {z}x^2 =$", rf"${w*z-1}x - {w}$" "\n\n"
         rf"$(x+{w})({z}x-1) = {z}x^2 - x + {w*z}x - {w} = {z}x^2 + {w*z-1}x - {w}$, puis on retranche ${z}x^2$."),
    ])

    # Q5 — factoriser
    p1 = r.randint(2, 6); p2 = r.choice([5, 6, 7, 8, 9, 11])
    g1 = r.randint(2, 7); g2 = r.randint(3, 9)
    c5 = r.choice([3, 4, 5, 6, 7])
    k5 = r.choice([2, 3, 5]); s5 = r.choice([2, 3, 4, 5, 6])
    q5 = q(5, 7, 1, "Factorise au maximum.", [
        ("a", rf"${p1*p1}x^2 - {p2*p2} =$", rf"$({p1}x+{p2})({p1}x-{p2})$" "\n\n"
         rf"Différence de deux carrés : $({p1}x)^2 - {p2}^2$."),
        ("b", rf"${g1}x^2 + {g1*g2}x =$", rf"${g1}x(x + {g2})$" "\n\n" rf"On met ${g1}x$ en évidence."),
        ("c", rf"$x^2 + {2*c5}x + {c5*c5} =$", rf"$(x + {c5})^2$" "\n\n"
         rf"Carré parfait : $x^2 + 2 \cdot {c5}x + {c5}^2$."),
        ("d", rf"${k5}x^2 - {k5*s5*s5} =$", rf"${k5}(x+{s5})(x-{s5})$" "\n\n"
         rf"On met d'abord ${k5}$ en évidence : ${k5}(x^2 - {s5*s5})$, puis on factorise la différence de carrés."),
    ])

    # Q6 — transformer une formule
    formules6 = [
        (r"V = \frac{\pi r^2 h}{3}", "le volume d'un cône", "h", r"h = \frac{3V}{\pi r^2}",
         r"On multiplie les deux membres par $3$ : $3V = \pi r^2 h$, puis on divise par $\pi r^2$."),
        (r"A = \frac{(B + b) \cdot h}{2}", "l'aire d'un trapèze", "h", r"h = \frac{2A}{B + b}",
         r"On multiplie par $2$ : $2A = (B+b) \cdot h$, puis on divise par $B+b$."),
        (r"V = \frac{\mathcal{B} \cdot h}{3}", "le volume d'une pyramide", r"\mathcal{B}", r"\mathcal{B} = \frac{3V}{h}",
         r"On multiplie par $3$ : $3V = \mathcal{B} \cdot h$, puis on divise par $h$."),
        (r"V = \frac{4\pi r^3}{3}", "le volume d'une boule", "r^3", r"r^3 = \frac{3V}{4\pi}",
         r"On multiplie par $3$ : $3V = 4\pi r^3$, puis on divise par $4\pi$."),
        (r"A = \pi r^2", "l'aire d'un disque", "r^2", r"r^2 = \frac{A}{\pi}",
         r"On divise les deux membres par $\pi$."),
        (r"P = 2\pi r", "le périmètre d'un cercle", "r", r"r = \frac{P}{2\pi}",
         r"On divise les deux membres par $2\pi$."),
        (r"V = \mathcal{B} \cdot h", "le volume d'un prisme droit", r"\mathcal{B}", r"\mathcal{B} = \frac{V}{h}",
         r"On divise les deux membres par $h$."),
        (r"A = \frac{D \cdot d}{2}", "l'aire d'un losange", "d", r"d = \frac{2A}{D}",
         r"On multiplie par $2$ : $2A = D \cdot d$, puis on divise par $D$."),
        (r"A = c^2", "l'aire d'un carré", "c", r"c = \sqrt{A}",
         r"On prend la racine carrée des deux membres, le côté étant positif."),
        (r"V = \frac{\pi d^2 h}{4}", "le volume d'un cylindre à partir de son diamètre",
         "h", r"h = \frac{4V}{\pi d^2}",
         r"On multiplie par $4$ : $4V = \pi d^2 h$, puis on divise par $\pi d^2$."),
    ]
    choix = formules6[(variante - 1) % len(formules6)]
    q6 = q(6, 2, 1, "Transforme la formule.", [
        ("", rf"${choix[0]}$ donne {choix[1]}." "\n" rf"Exprime ${choix[2]}$ en fonction des autres grandeurs.",
         rf"${choix[3]}$" "\n\n" + choix[4]),
    ])

    # Q7 — aire par polynôme
    c7 = r.randint(3, 12)
    k7 = r.randint(2, 5)
    figures7 = [
        (rf"Un carré a pour côté $(x + {c7})$. On y découpe, dans un coin, un carré de "
         rf"côté $x$ que l'on retire.",
         rf"$A = {2*c7}x + {c7*c7}$",
         rf"Grand carré : $(x+{c7})^2 = x^2 + {2*c7}x + {c7*c7}$." "\n"
         rf"Carré retiré : $x^2$." "\n"
         rf"Différence : ${2*c7}x + {c7*c7}$."),
        (rf"Un rectangle mesure $({k7}x + {c7})$ de long et $x$ de large. On y découpe un "
         rf"carré de côté $x$ que l'on retire.",
         rf"$A = {coef(k7-1)}x^2 + {c7}x$",
         rf"Rectangle : $x({k7}x + {c7}) = {k7}x^2 + {c7}x$." "\n"
         rf"Carré retiré : $x^2$." "\n"
         rf"Différence : ${coef(k7-1)}x^2 + {c7}x$."),
        (rf"Un carré de côté $(x + {c7})$ est accolé à un rectangle de $x$ sur ${k7}$.",
         rf"$A = x^2 + {2*c7+k7}x + {c7*c7}$",
         rf"Carré : $(x+{c7})^2 = x^2 + {2*c7}x + {c7*c7}$." "\n"
         rf"Rectangle : ${k7}x$." "\n"
         rf"Somme : $x^2 + {2*c7+k7}x + {c7*c7}$."),
        (rf"D'un rectangle de $({k7}x + {c7})$ sur ${k7}$, on retire un carré de côté ${k7}$.",
         rf"$A = {k7*k7}x + {k7*c7 - k7*k7}$",
         rf"Rectangle : ${k7}({k7}x + {c7}) = {k7*k7}x + {k7*c7}$." "\n"
         rf"Carré retiré : ${k7*k7}$." "\n"
         rf"Différence : ${k7*k7}x + {k7*c7 - k7*k7}$."),
    ]
    enonce7, rep7, just7 = figures7[(variante - 1) % len(figures7)]
    q7 = q(7, 4, 1, "Exprime l'aire à l'aide d'un polynôme réduit.", [
        ("", enonce7 + "\n" + "Exprime l'aire $A$ de la surface obtenue à l'aide d'un polynôme réduit.",
         rep7 + "\n\n" + just7),
    ])

    # Q8 — tour de magie
    ajout = r.randint(3, 19); mult8 = r.randint(2, 7)
    q8 = q(8, 3, 2, "Résous le problème.", [
        ("", rf"Un magicien demande à une spectatrice de penser à un nombre, d'y ajouter ${ajout}$, "
             rf"de multiplier le résultat par ${mult8}$, puis de retrancher ${mult8}$ fois le nombre de départ." "\n"
             rf"Le magicien annonce le résultat sans rien demander. Quel est-il ? Justifie.",
         rf"${ajout*mult8}$, quel que soit le nombre choisi." "\n\n"
         rf"Soit $n$ le nombre pensé." "\n"
         rf"${mult8}(n + {ajout}) - {mult8}n = {mult8}n + {ajout*mult8} - {mult8}n = {ajout*mult8}$." "\n"
         rf"Le nombre de départ disparaît : le résultat vaut toujours ${ajout*mult8}$."),
    ])

    # Q9 — équation à dénominateurs
    # On part de la solution et on choisit b pour que le membre de gauche soit
    # entier : l'équation est alors résoluble par construction, sans recherche.
    sol = r.randint(2, 15)
    c9, f9 = r.choice([(3, 2), (4, 3), (2, 5), (5, 2), (3, 4)])
    a9 = r.randint(2, 4)
    d9 = r.randint(1, 4)
    b9 = (-a9 * sol) % c9          # rend a9·sol + b9 divisible par c9
    if b9 > c9 // 2: b9 -= c9      # garde un coefficient de taille raisonnable
    gauche = F(a9 * sol + b9, c9) + d9
    e9 = int(gauche * f9 - sol)
    # b nul donnerait « 3x + 0 » : on omet simplement le terme.
    # b nul donnerait « 3x + 0 » : on omet simplement le terme.
    terme_b = "" if b9 == 0 else (f" + {b9}" if b9 > 0 else f" - {-b9}")
    signe_e = f"+ {e9}" if e9 >= 0 else f"- {-e9}"
    q9 = q(9, 3, 2, "Résous l'équation.", [
        ("", rf"$\frac{{{a9}x{terme_b}}}{{{c9}}} + {d9} = \frac{{x {signe_e}}}{{{f9}}}$",
         rf"$x = {sol}$" "\n\n"
         rf"On multiplie tout par ${c9*f9}$, puis on regroupe." "\n"
         rf"Vérification : à gauche $\frac{{{a9*sol+b9}}}{{{c9}}} + {d9} = {frac(gauche)}$, "
         rf"à droite $\frac{{{sol+e9}}}{{{f9}}} = {frac(F(sol+e9, f9))}$ ✓."),
    ])

    # Q10 — solide et volume
    base10 = r.choice([("hexagonales", "six", "hexagonale"), ("pentagonales", "cinq", "pentagonale"),
                       ("triangulaires", "trois", "triangulaire")])
    aire10, h10 = r.randint(12, 40), r.randint(5, 14)
    q10 = q(10, 5, 2, "Identifie et calcule.", [
        ("a", rf"Un solide a deux bases {base10[0]} identiques et parallèles, "
              rf"reliées par {base10[1]} faces rectangulaires. Quel est son nom ?",
         rf"Un prisme droit à base {base10[2]}." "\n\n"
         r"Deux bases identiques et parallèles reliées par des rectangles caractérisent un prisme droit."),
        ("b", rf"Son aire de base vaut ${aire10}$ $\mathrm{{cm}}^2$ et sa hauteur ${h10}$ cm. Calcule son volume.",
         rf"${aire10*h10}$ $\mathrm{{cm}}^3$" "\n\n" rf"$V = \mathcal{{B}} \cdot h = {aire10} \cdot {h10} = {aire10*h10}$."),
    ])

    # Q11 — volume composé cylindre + demi-boule
    r11, h11 = r.randint(2, 9), r.randint(6, 20)
    vol11 = math.pi*r11*r11*h11 + 0.5*(4*math.pi*r11**3/3)
    coef_cyl, coef_demi = r11*r11*h11, F(2*r11**3, 3)
    q11 = q(11, 6, 2, "Calcule et arrondis au centième.", [
        ("", rf"Un solide est composé d'un cylindre de rayon ${r11}$ cm et de hauteur ${h11}$ cm, "
             rf"surmonté d'une demi-boule de même rayon." "\n"
             rf"Calcule son volume total en $\mathrm{{cm}}^3$, arrondi au centième." "\n"
             rf"On rappelle que le volume d'une boule vaut $\frac{{4\pi r^3}}{{3}}$.",
         rf"${virg(round(vol11,2),2)}$ $\mathrm{{cm}}^3$" "\n\n"
         rf"Cylindre : $\pi \cdot {r11}^2 \cdot {h11} = {coef_cyl}\pi$." "\n"
         rf"Demi-boule : $\frac{{1}}{{2}} \cdot \frac{{4\pi \cdot {r11**3}}}{{3}} = {frac(coef_demi)}\pi$." "\n"
         rf"Total : ${frac(coef_cyl + coef_demi)}\pi \approx {virg(round(vol11,2),2)}$ $\mathrm{{cm}}^3$."),
    ])

    # Q12 — pyramide et fraction de remplissage
    # Le volume est calculé d'abord ; la fraction de remplissage est ensuite
    # choisie parmi celles qui le divisent, plutôt que tirée puis rattrapée.
    cote12 = r.choice([4, 6, 8, 10])
    h12 = r.choice([6, 9, 12, 15])
    v12 = F(cote12 * cote12 * h12, 3)
    candidates = [(n, d) for n, d in ((2,3), (3,4), (1,2), (2,5), (3,5))
                  if (F(n, d) * v12).denominator == 1]
    num12, den12 = r.choice(candidates) if candidates else (1, 2)
    jus = F(num12, den12) * v12
    q12 = q(12, 4, 2, "Calcule.", [
        ("", rf"Un verre a la forme d'une pyramide à base carrée posée sur sa pointe. "
             rf"Le côté de sa base carrée mesure ${cote12}$ cm et sa hauteur ${h12}$ cm." "\n"
             rf"a) Calcule le volume total du verre." "\n"
             rf"b) On le remplit de jus aux ${fr(num12,den12)}$ de son volume. Quel volume de jus contient-il ?",
         rf"a) ${int(v12)}$ $\mathrm{{cm}}^3$" "\n\n" rf"$V = \frac{{\mathcal{{B}} \cdot h}}{{3}} = \frac{{{cote12*cote12} \cdot {h12}}}{{3}} = {int(v12)}$." "\n\n"
         rf"b) ${int(jus)}$ $\mathrm{{cm}}^3$" "\n\n" rf"${fr(num12,den12)} \cdot {int(v12)} = {int(jus)}$."),
    ])

    # Q13 — réciproque dans un quadrilatère
    t13 = r.choice(TRIPLETS)
    S = r.choice([("A","B","C","D"),("E","F","G","H"),("K","L","M","N"),("P","Q","R","S")])
    q13 = q(13, 3, 2, "Justifie ta réponse.", [
        ("", rf"${S[0]}{S[1]}{S[2]}{S[3]}$ est un quadrilatère tel que ${S[0]}{S[1]} = {t13[0]}$ cm, "
             rf"${S[1]}{S[2]} = {t13[1]}$ cm et la diagonale ${S[0]}{S[2]} = {t13[2]}$ cm." "\n"
             rf"Le triangle ${S[0]}{S[1]}{S[2]}$ est-il rectangle ? Si oui, en quel sommet ? Justifie.",
         rf"Oui, rectangle en ${S[1]}$." "\n\n"
         rf"Le plus grand côté est ${S[0]}{S[2]} = {t13[2]}$." "\n"
         rf"${t13[0]}^2 + {t13[1]}^2 = {t13[0]**2} + {t13[1]**2} = {t13[2]**2}$ et ${t13[2]}^2 = {t13[2]**2}$." "\n"
         rf"Par la réciproque du théorème de Pythagore, le triangle est rectangle, "
         rf"et l'angle droit est opposé à $[{S[0]}{S[2]}]$, donc en ${S[1]}$."),
    ])

    questions = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13]
    epreuve = {"id": f"evacom-ls-{variante}", "niveau": "LS",
               "titre": f"EVACOM blanc n° {variante} — section LS",
               "questions": questions}
    # Une question de plus, dont le thème tourne, pour couvrir les
    # absences relevées dans les sept dernières années d'épreuves.
    return complements.ajouter(epreuve, "LS", variante, r)
