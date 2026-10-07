# -*- coding: utf-8 -*-
"""Recalcule chaque résultat annoncé, à partir des seuls énoncés produits."""
import re, math, sys
from fractions import Fraction as F
sys.path.insert(0, '/tmp/evacom')

def tete(sq): return sq["reponse"].split("\n")[0]
def nombres(t): return [int(x) for x in re.findall(r"-?\d+", t)]

def verifier(e):
    pbs = []
    # La question de complément décale les numéros : on réindexe sur les
    # seules questions du squelette d'origine.
    originales = [q for q in e["questions"] if not q.get("complement")]
    Q = {i + 1: q for i, q in enumerate(originales)}

    # Q1 relatifs : on rejoue chaque calcul depuis l'énoncé
    for sq in Q[1]["sousQuestions"]:
        m = re.match(r"\$\(([+-])(\d+)\) ?(\\cdot|:|\+|-) ?\(([+-])(\d+)\)", sq["enonce"])
        s1, n1, op, s2, n2 = m.groups()
        a = int(s1 + n1); b = int(s2 + n2)
        attendu = {"+": a+b, "-": a-b, "\\cdot": a*b, ":": a//b if a*b>0 else -((-a)//b if a<0 else a//(-b))}[op]
        if op == ":": attendu = int(F(a, b))
        obtenu = nombres(tete(sq))[0]
        if obtenu != attendu: pbs.append(f"Q1{sq['libelle']} : annoncé {obtenu}, calculé {attendu}")

    # Q2 fractions
    for sq, oper in zip(Q[2]["sousQuestions"], ("*", "/")):
        f = [F(int(a), int(b)) for a, b in re.findall(r"\\frac\{(\d+)\}\{(\d+)\}", sq["enonce"])]
        attendu = f[0]*f[1] if oper == "*" else f[0]/f[1]
        t = re.search(r"\\frac\{(-?\d+)\}\{(\d+)\}", tete(sq))
        obtenu = F(int(t.group(1)), int(t.group(2))) if t else F(nombres(tete(sq))[0])
        if obtenu != attendu: pbs.append(f"Q2{sq['libelle']} : annoncé {obtenu}, calculé {attendu}")

    # Q3 compléter
    a = Q[3]["sousQuestions"][0]
    f = re.findall(r"\\frac\{(\d+)\}\{(\d+)\}", a["enonce"])
    if int(f[-1][0]) - int(f[0][0]) != nombres(tete(a))[0]:
        pbs.append(f"Q3a : annoncé {nombres(tete(a))[0]}, calculé {int(f[-1][0])-int(f[0][0])}")

    # Q8 / Q9 Pythagore
    for num, mode in ((8, "hyp"), (9, "cat")):
        sq = Q[num]["sousQuestions"][0]
        ns = nombres(sq["enonce"])
        if mode == "hyp":
            attendu = math.isqrt(ns[0]**2 + ns[1]**2)
            if attendu**2 != ns[0]**2 + ns[1]**2: pbs.append(f"Q{num} : triplet non pythagoricien")
        else:
            attendu = math.isqrt(ns[0]**2 - ns[1]**2)
            if attendu**2 != ns[0]**2 - ns[1]**2: pbs.append(f"Q{num} : triplet non pythagoricien")
        if nombres(tete(sq))[0] != attendu:
            pbs.append(f"Q{num} : annoncé {nombres(tete(sq))[0]}, calculé {attendu}")

    # Q11 volume du cylindre
    sq = Q[11]["sousQuestions"][0]
    ra, ha = nombres(sq["enonce"])[:2]
    attendu = round(math.pi*ra*ra*ha, 1)
    obtenu = float(re.search(r"\$([\d]+)\{,\}(\d)\$", tete(sq)).group(1) + "." + re.search(r"\$([\d]+)\{,\}(\d)\$", tete(sq)).group(2))
    if abs(obtenu - attendu) > 0.05: pbs.append(f"Q11 : annoncé {obtenu}, calculé {attendu}")

    # Q12 cohérence du moule choisi
    sq = Q[12]["sousQuestions"][0]
    ns = nombres(sq["enonce"])
    arete, d1, d2, d3, litres = ns[0], ns[1], ns[2], ns[3], ns[4]
    va, vb = arete**3, d1*d2*d3
    attendu = "A" if (litres*1000)//va > (litres*1000)//vb else "B"
    if f"moule {attendu}" not in tete(sq): pbs.append(f"Q12 : annoncé {tete(sq)}, calculé moule {attendu}")

    # Q13 longueur de fil
    sq = Q[13]["sousQuestions"][0]
    n, a, libre = nombres(sq["enonce"])[:3]
    attendu = F(n*a + 2*libre, 10)
    t = tete(sq).replace("{,}", ".")
    obtenu = F(str(re.search(r"\$([\d.]+)\$", t).group(1)))
    if obtenu != attendu: pbs.append(f"Q13 : annoncé {obtenu}, calculé {attendu}")

    return pbs

if __name__ == "__main__":
    from gen_ct import engendrer
    total = 0
    for v in range(1, 11):
        e = engendrer(v)
        pbs = verifier(e)
        total += len(pbs)
        print(f"  {'✓' if not pbs else '✗'} épreuve {v:>2} — {sum(q['points'] for q in e['questions'])} pts")
        for p in pbs: print(f"       ⚠ {p}")
    print(f"\n10 épreuves CT vérifiées, {total} problème(s)")
