# -*- coding: utf-8 -*-
from fractions import Fraction as F
import math
c = [
 ("Q1a 5/6-3/8",        F(5,6)-F(3,8),        F(11,24)),
 ("Q1b 14/9:7/6",       F(14,9)/F(7,6),       F(4,3)),
 ("Q1c 15/8*12/25",     F(15,8)*F(12,25),     F(9,10)),
 ("Q1d 49/sqrt49",      49//int(math.isqrt(49)), 7),
 ("Q2a 3/4+5/8+x=2",    2-F(3,4)-F(5,8),      F(5,8)),   # x/8 donc x=5
 ("Q2b sqrt(x)+3=10",   (10-3)**2,            49),
 ("Q2c x/6=10/15",      F(10,15)*6,           4),
 ("Q3  héritage",       F(3*12000,3)*4,       48000),
 ("Q4b (x+3)(x+4)",     (3+4, 3*4),           (7,12)),
 ("Q5  (3x+2)(3x-2)",   -4,                   -4),
 ("Q7  Léa",            15,                   15),
 ("Q7  Tom = l+6",      15+6,                 21),
 ("Q7  contrôle 1",     15+3 == 21-3,         True),
 ("Q7  contrôle 2",     21+3 == 2*(15-3),     True),
 ("Q9  2a+4b-c",        2*4+4*2.5-(-3),       21),
 ("Q10 2x+16=6x",       F(16,4),              4),
 ("Q10 périm rect x=4", 2*(4+2)+2*6,          24),
 ("Q10 périm tri x=4",  3*2*4,                24),
 ("Q11 24,32,40",       24**2+32**2 == 40**2, True),
 ("Q12 20,21,29",       20**2+21**2 == 29**2, True),
 ("Q13 losange d",      F(84*2,14),           12),
 ("Q14 (8/3)x=1600",    F(1600*3,8),          600),
]
err=0
for n,a,b in c:
    ok = a==b
    if not ok: err+=1
    print(f"  {'✓' if ok else '✗'} {n:22} calculé={a}  annoncé={b}")
print(f"\n{len(c)} contrôles, {err} erreur(s)")
