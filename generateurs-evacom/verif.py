# -*- coding: utf-8 -*-
"""Recalcule indépendamment chaque résultat annoncé dans l'épreuve."""
from fractions import Fraction as F
import math

controles = [
    ("Q1a  (+42)+(-57)",            42 + (-57),            -15),
    ("Q1b  (+36)-(-14)",            36 - (-14),             50),
    ("Q1c  (-6)*(-9)",              -6 * -9,                54),
    ("Q1d  (-48)/(+6)",             -48 // 6,               -8),
    ("Q2a  8/15 * 5/12",            F(8,15)*F(5,12),        F(2,9)),
    ("Q2b  9/14 : 3/7",             F(9,14)/F(3,7),         F(3,2)),
    ("Q3a  5/12 + 6/12",            F(5,12)+F(6,12),        F(11,12)),
    ("Q3b  3/4 * 3/5",              F(3,4)*F(3,5),          F(9,20)),
    ("Q3c  7/10 - 3/5",             F(7,10)-F(3,5),         F(1,10)),
    ("Q5a  3/5 * 1/4",              F(3,5)*F(1,4),          F(3,20)),
    ("Q5b  3/20 de 600",            F(3,20)*600,            90),
    ("Q8   hypoténuse 9,12",        math.isqrt(9**2+12**2), 15),
    ("Q9a  côté 13,5",              math.isqrt(13**2-5**2), 12),
    ("Q9b  aire 12*5",              12*5,                   60),
    ("Q10  vitesse rouge",          F(144)/F(3,2),          96),
    ("Q10  vitesse verte",          100,                    100),
    ("Q11  volume cylindre",        round(math.pi*25*12,1), 942.5),
    ("Q12  volume cube 4",          4**3,                   64),
    ("Q12  volume pavé 5*4*3",      5*4*3,                  60),
    ("Q12  3000/64 entier",         3000//64,               46),
    ("Q12  3000/60 entier",         3000//60,               50),
    ("Q13  fil total mm",           25*8 + 2*15,            230),
    ("Q13  en cm",                  F(230,10),              23),
]
erreurs = 0
for nom, calcule, annonce in controles:
    ok = calcule == annonce
    if not ok: erreurs += 1
    print(f"  {'✓' if ok else '✗'} {nom:28} calculé={calcule}  annoncé={annonce}")
print(f"\n{len(controles)} contrôles, {erreurs} erreur(s)")
