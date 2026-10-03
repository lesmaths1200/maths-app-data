# -*- coding: utf-8 -*-
import re, sys, math
from fractions import Fraction as F
sys.path.insert(0, '/tmp/evacom')
from gen_lc import engendrer

def tete(sq): return sq["reponse"].split("\n")[0]
def ints(t): return [int(x) for x in re.findall(r"-?\d+", t)]
def lire_frac(t):
    m = re.search(r"\\frac\{(-?\d+)\}\{(\d+)\}", t)
    if m: return F(int(m.group(1)), int(m.group(2)))
    n = ints(t)
    return F(n[0]) if n else None

def verifier(e):
    p = []
    Q = {q["numero"]: q for q in e["questions"]}

    fs = Q[1]["sousQuestions"]
    for sq, op in zip(fs[:3], ("-", "/", "*")):
        f = [F(int(a), int(b)) for a, b in re.findall(r"\\frac\{(\d+)\}\{(\d+)\}", sq["enonce"])]
        att = {"-": f[0]-f[1], "/": f[0]/f[1], "*": f[0]*f[1]}[op]
        if lire_frac(tete(sq)) != att: p.append(f"Q1{sq['libelle']} : {lire_frac(tete(sq))} ≠ {att}")
    sq = fs[3]; car = ints(sq["enonce"])[0]
    if ints(tete(sq))[0] != math.isqrt(car): p.append(f"Q1d : racine")

    # Q2a : le numérateur manquant
    sq = Q[2]["sousQuestions"][0]
    f = re.findall(r"\\frac\{(\d+)\}\{(\d+)\}", sq["enonce"])
    # le terme inconnu s'écrit \frac{\square}{dd} : il échappe au motif ci-dessus
    dd = int(re.search(r"\\frac\{\\square\}\{(\d+)\}", sq["enonce"]).group(1))
    cible = ints(sq["enonce"].split("=")[-1])[0]
    somme = sum(F(int(a), int(b)) for a, b in f)
    att = (F(cible) - somme) * dd
    if ints(tete(sq))[0] != att: p.append(f"Q2a : {ints(tete(sq))[0]} ≠ {att}")

    # Q3 : héritage
    sq = Q[3]["sousQuestions"][0]
    nb = {"Trois":3,"Quatre":4,"Cinq":5}[sq["enonce"].split()[0]]
    den = {"tiers":3,"quart":4,"cinquième":5}[re.search(r"le (tiers|quart|cinquième)", sq["enonce"]).group(1)]
    part = ints(re.search(r"chacun", sq["enonce"]).string.split("CHF")[1])[0]
    att = F(nb*part*den, den-1)
    if ints(tete(sq))[0] != att: p.append(f"Q3 : {ints(tete(sq))[0]} ≠ {att}")

    # Q10 : périmètres
    sq = Q[10]["sousQuestions"][0]
    dec, cote = ints(sq["enonce"])[:2]
    att = F(2*dec + 2*cote, 4)
    if ints(tete(sq))[0] != att: p.append(f"Q10 : {ints(tete(sq))[0]} ≠ {att}")

    # Q11 / Q12 : triplets
    for n in (11, 12):
        v = ints(Q[n]["sousQuestions"][0]["enonce"])
        a, b, c = (v[0], v[1], v[2]) if n == 11 else (v[0], v[1], v[2])
        if a*a + b*b != c*c: p.append(f"Q{n} : {a},{b},{c} non pythagoricien")

    # Q13 : losange
    sq = Q[13]["sousQuestions"][0]
    t = sq["enonce"].replace("{,}", ".")
    aire = float(re.search(r"aire de \$([\d.]+)\$", t).group(1))
    D = int(re.search(r"diagonale mesure \$(\d+)\$", t).group(1))
    att = F(round(aire*2)) / D if (aire*2) % D == 0 else F(aire*2).limit_denominator()/D
    if abs(float(ints(tete(sq))[0]) - aire*2/D) > 1e-9: p.append(f"Q13 : {ints(tete(sq))[0]} ≠ {aire*2/D}")

    # Q14 : investissement
    sq = Q[14]["sousQuestions"][0]
    perte = {"tiers":3,"quart":4,"cinquième":5}[re.search(r"perd le (tiers|quart|cinquième)", sq["enonce"]).group(1)]
    fact = {"triple":3,"quadruple":4,"quintuple":5,"sextuple":6}[re.search(r"(triple|quadruple|quintuple|sextuple)", sq["enonce"]).group(1)]
    total = int(re.search(r"atteint alors CHF \$\\,(\d+)\$", sq["enonce"]).group(1))
    att = F(total * perte, fact * (perte-1))
    if ints(tete(sq))[0] != att: p.append(f"Q14 : {ints(tete(sq))[0]} ≠ {att}")
    return p

total = 0
for v in range(1, 11):
    e = engendrer(v); pbs = verifier(e); total += len(pbs)
    print(f"  {'✓' if not pbs else '✗'} épreuve {v:>2} — {sum(q['points'] for q in e['questions'])} pts")
    for x in pbs: print(f"       ⚠ {x}")
print(f"\n10 épreuves LC vérifiées, {total} problème(s)")
