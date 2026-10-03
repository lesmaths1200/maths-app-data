# -*- coding: utf-8 -*-
from fractions import Fraction as F
import math, re
c = [
 ("Q1a sqrt8*sqrt2",    math.isqrt(8*2),        4),
 ("Q1b sqrt48/sqrt3",   math.isqrt(48//3),      4),
 ("Q1c (√5+2)(√5-2)",   5-4,                    1),
 ("Q1d 7/12+5/18",      F(7,12)+F(5,18),        F(31,36)),
 ("Q2a √50=5√2",        (5, 2), (5, 50//25)),
 ("Q2b √98=7√2",        (7, 2), (7, 98//49)),
 ("Q2c √108=6√3",       6*6*3,                  108),
 ("Q3a 6²<40<7²",       36 < 40 < 49,           True),
 ("Q3b (-3)^4",         (-3)**4,                81),
 ("Q4a (2x-3)² coefs",  (4, -12, 9),            (2**2, -2*2*3, 9)),
 ("Q4b (x+4)(2x-1)",    (2, 7, -4),             (2, -1+8, -4)),
 ("Q5a 9x²-49",         (3*3, 7*7),             (9, 49)),
 ("Q5d 3(x²-9)",        3*9,                    27),
 ("Q7  (x+6)²-x²",      (12, 36),               (2*6, 36)),
 ("Q8  3(n+7)-3n",      3*(13+7)-3*13,          21),
 ("Q9  équation",       None,                   None),
 ("Q10b 24*7",          24*7,                   168),
 ("Q11 cylindre 90π",   round(math.pi*9*10, 6), round(90*math.pi, 6)),
 ("Q11 demi-boule 18π", round(0.5*4*math.pi*27/3, 6), round(18*math.pi, 6)),
 ("Q11 total arrondi",  round(108*math.pi, 2),  339.29),
 ("Q12a pyramide",      F(36*9,3),              108),
 ("Q12b 2/3 de 108",    F(2,3)*108,             72),
 ("Q13 9,40,41",        9**2+40**2 == 41**2,    True),
]
err=0
for n,a,b in c:
    if a is None:
        # équation (2x-1)/3 + 2 = (x+7)/2
        from sympy import symbols, Eq, solve, Rational
        x=symbols('x'); s=solve(Eq(Rational(1,3)*(2*x-1)+2, Rational(1,2)*(x+7)), x)
        a,b = s[0], s[0]
        print(f"  ℹ {n:22} solution réelle = {a}")
        continue
    ok = a==b
    if not ok: err+=1
    print(f"  {'✓' if ok else '✗'} {n:22} calculé={a}  annoncé={b}")
print(f"\n{len(c)-1} contrôles, {err} erreur(s)")
