# -*- coding: utf-8 -*-
import re, sys, math
from fractions import Fraction as F
sys.path.insert(0, '/tmp/evacom')
from gen_ls import engendrer

def tete(sq): return sq["reponse"].split("\n")[0]
def ints(t):
    # « cm$^3$ » et « x^2 » contiennent des chiffres qui ne sont pas des données :
    # on retire les exposants avant d'extraire les nombres.
    t = re.sub(r"\^\{?-?\d+\}?", "", t)
    t = re.sub(r"cm\$?\^?\d?\$?", "", t)
    return [int(x) for x in re.findall(r"-?\d+", t)]

def verifier(e):
    p = []
    Q = {q["numero"]: q for q in e["questions"]}
    xs = [F(-5), F(-1,2), F(0), F(2,3), F(4), F(9)]

    # Q1 racines et somme de fractions
    s = Q[1]["sousQuestions"]
    a, b = ints(s[0]["enonce"])[:2]
    if ints(tete(s[0]))[0]**2 != a*b: p.append(f"Q1a : {ints(tete(s[0]))[0]}² ≠ {a*b}")
    n, d = ints(s[1]["enonce"])[:2]
    if ints(tete(s[1]))[0]**2 != n//d: p.append(f"Q1b")
    rr, ee = ints(s[2]["enonce"])[:2]
    if ints(tete(s[2]))[0] != rr - ee*ee: p.append(f"Q1c")
    f = [F(int(x), int(y)) for x, y in re.findall(r"\\frac\{(\d+)\}\{(\d+)\}", s[3]["enonce"])]
    att = f[0] + f[1]
    m = re.search(r"\\frac\{(\d+)\}\{(\d+)\}", tete(s[3]))
    got = F(int(m.group(1)), int(m.group(2))) if m else F(ints(tete(s[3]))[0])
    if got != att: p.append(f"Q1d : {got} ≠ {att}")

    # Q2 extraction de racines
    for sq in Q[2]["sousQuestions"]:
        n = ints(sq["enonce"]); sous = n[0]*n[1] if len(n) > 1 and "\\cdot" in sq["enonce"] else n[0]
        aa, bb = ints(tete(sq))[:2]
        if aa*aa*bb != sous: p.append(f"Q2{sq['libelle']} : {aa}²·{bb} ≠ {sous}")

    # Q3a encadrement
    sq = Q[3]["sousQuestions"][0]; n3 = ints(sq["enonce"])[0]; lo, hi = ints(tete(sq))[:2]
    if not (lo*lo < n3 < hi*hi and hi == lo+1): p.append(f"Q3a : {lo},{hi} pour √{n3}")

    # Q4 / Q5 / Q7 identités, évaluées numériquement
    def ev(expr, x):
        return eval(expr.replace("^", "**"), {"x": x, "F": F})
    s4 = Q[4]["sousQuestions"]
    u, v = ints(s4[0]["enonce"])[:2]; ca, cb, cc = ints(tete(s4[0]))[:3]
    if not all(( (u*x - v)**2 == ca*x*x - cb*x + cc for x in xs)): p.append("Q4a")
    w, z = ints(s4[1]["enonce"])[:2]; k1, k2 = ints(tete(s4[1]))[:2]
    if not all(((x + w)*(z*x - 1) - z*x*x == k1*x - k2 for x in xs)): p.append("Q4b")

    s5 = Q[5]["sousQuestions"]
    A, B = ints(s5[0]["enonce"])[:2]; a5, b5 = ints(tete(s5[0]))[:2]
    if not all((A*x*x - B == (a5*x+b5)*(a5*x-b5) for x in xs)): p.append("Q5a")
    g1, g2 = ints(s5[1]["enonce"])[:2]; h1, h2 = ints(tete(s5[1]))[:2]
    if not all((g1*x*x + g2*x == h1*x*(x+h2) for x in xs)): p.append("Q5b")
    c1, c2 = ints(s5[2]["enonce"])[:2]; c5 = ints(tete(s5[2]))[0]
    if not all((x*x + c1*x + c2 == (x+c5)**2 for x in xs)): p.append("Q5c")
    k5, ks = ints(s5[3]["enonce"])[:2]; m5, s5v = ints(tete(s5[3]))[:2]
    if not all((k5*x*x - ks == m5*(x+s5v)*(x-s5v) for x in xs)): p.append("Q5d")

    sq = Q[7]["sousQuestions"][0]; c7 = ints(sq["enonce"])[0]; d7, e7 = ints(tete(sq))[:2]
    if not all(((x+c7)**2 - x*x == d7*x + e7 for x in xs)): p.append("Q7")

    # Q8 tour de magie
    sq = Q[8]["sousQuestions"][0]; aj, mu = ints(sq["enonce"])[:2]
    if ints(tete(sq))[0] != aj*mu: p.append("Q8")

    # Q9 équation : on substitue la solution annoncée
    sq = Q[9]["sousQuestions"][0]
    # le terme constant peut être absent quand il vaut zéro
    m = re.match(r"\$\\frac\{(\d+)x(?: ([+-]) (\d+))?\}\{(\d+)\} \+ (\d+) = \\frac\{x ([+-]) (\d+)\}\{(\d+)\}\$", sq["enonce"])
    if m:
        a9, sb, b9, c9, d9, se, e9, f9 = m.groups()
        b9 = 0 if b9 is None else int(b9)*(1 if sb=="+" else -1)
        a9, c9, d9, e9, f9 = int(a9), int(c9), int(d9), int(e9)*(1 if se=="+" else -1), int(f9)
        x9 = ints(tete(sq))[0]
        if F(a9*x9 + b9, c9) + d9 != F(x9 + e9, f9): p.append(f"Q9 : x={x9} ne vérifie pas l'équation")
    else:
        p.append("Q9 : énoncé non analysable")

    # Q10b, Q12, Q13
    sq = Q[10]["sousQuestions"][1]; ai, hh = ints(sq["enonce"])[:2]
    if ints(tete(sq))[0] != ai*hh: p.append("Q10b")
    sq = Q[12]["sousQuestions"][0]; co, ha = ints(sq["enonce"])[:2]
    v12 = F(co*co*ha, 3); a12 = ints(tete(sq))[0]
    if a12 != v12: p.append(f"Q12a : {a12} ≠ {v12}")
    sq = Q[13]["sousQuestions"][0]; t = ints(sq["enonce"])
    if t[0]**2 + t[1]**2 != t[2]**2: p.append("Q13 : triplet")
    return p

total = 0
for v in range(1, 11):
    e = engendrer(v); pbs = verifier(e); total += len(pbs)
    print(f"  {'✓' if not pbs else '✗'} épreuve {v:>2} — {sum(q['points'] for q in e['questions'])} pts")
    for x in pbs: print(f"       ⚠ {x}")
print(f"\n10 épreuves LS vérifiées, {total} problème(s)")
