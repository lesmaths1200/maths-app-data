# -*- coding: utf-8 -*-
"""Une question de plus par épreuve, pour couvrir les thèmes qui manquaient.

L'analyse des sept dernières années a montré des absences : les fractions et
les angles en LS, la vitesse en LC, les pourcentages en LS et CT… Plutôt que
d'alourdir chaque épreuve de quatre questions, on en ajoute **une seule**,
dont le thème tourne d'une variante à l'autre. Sur dix épreuves, chaque
lacune est ainsi comblée deux ou trois fois.
"""
from fractions import Fraction as F


def fr(n, d): return rf"\frac{{{n}}}{{{d}}}"


def _question(numero, points, partie, theme, consigne, sous):
    return {"numero": numero, "points": points, "partie": partie, "theme": theme,
            # Marque la question ajoutée : elle décale la numérotation, et les
            # contrôles doivent pouvoir retrouver les questions d'origine.
            "complement": True, "consigne": consigne,
            "sousQuestions": [{"libelle": l, "enonce": e, "reponse": r} for l, e, r in sous]}


# ─────────────────────────────── fabriques ────────────────────────────────

def fractions(r):
    a, b = r.choice([(5,6),(7,12),(11,15),(7,10),(13,20),(9,14)])
    c, d = r.choice([(3,8),(5,18),(4,15),(3,10),(7,20),(5,21)])
    somme, diff = F(a,b) + F(c,d), F(a,b) - F(c,d)
    return (3, 1, "Fractions",
            "Calcule et donne la réponse sous forme d'une fraction irréductible.",
            [("a", rf"${fr(a,b)} + {fr(c,d)} =$",
              rf"${fr(somme.numerator, somme.denominator)}$" "\n\n"
              rf"Au dénominateur commun, la somme vaut ${fr(somme.numerator, somme.denominator)}$."),
             ("b", rf"${fr(a,b)} - {fr(c,d)} =$",
              rf"${fr(diff.numerator, diff.denominator)}$" "\n\n"
              rf"Même dénominateur commun, puis on soustrait les numérateurs.")])


def angles(r):
    base = r.choice([35, 42, 48, 54, 63, 27, 39, 51])
    sommet = 180 - 2 * base
    return (3, 1, "Angles",
            "Résous le problème.",
            [("", rf"Un triangle $ABC$ est isocèle en $A$. Ses angles à la base mesurent "
                  rf"${base}^\circ$." "\n"
                  rf"a) Calcule l'angle au sommet $\widehat{{A}}$." "\n"
                  rf"b) Ce triangle peut-il être rectangle ? Justifie.",
              rf"a) ${sommet}^\circ$" "\n\n"
              rf"La somme des angles vaut $180^\circ$ : "
              rf"$\widehat{{A}} = 180^\circ - {base}^\circ - {base}^\circ = {sommet}^\circ$." "\n\n"
              + (rf"b) Oui : l'angle au sommet mesure exactement $90^\circ$."
                 if sommet == 90 else
                 rf"b) Non : aucun de ses angles ne mesure $90^\circ$. "
                 rf"Il le serait si les angles à la base valaient $45^\circ$."))])


def pourcentages(r):
    # On choisit le taux d'abord, puis un prix qui donne un résultat entier :
    # incrémenter le prix ne changeait jamais le reste, et la boucle tournait
    # indéfiniment.
    taux = r.choice([10, 15, 20, 25, 30, 40])
    candidats = [p for p in range(60, 301, 10) if p * taux % 100 == 0]
    prix = r.choice(candidats)
    reduit = prix * (100 - taux) // 100
    return (3, 2, "Pourcentages",
            "Résous le problème.",
            [("", rf"Un article coûte CHF ${prix}$. Le magasin applique une réduction de "
                  rf"${taux}\%$." "\n"
                  rf"a) Quel est le montant de la réduction ?" "\n"
                  rf"b) Quel est le prix à payer ?",
              rf"a) CHF ${prix * taux // 100}$" "\n\n"
              rf"$\frac{{{taux}}}{{100}} \cdot {prix} = {prix * taux // 100}$." "\n\n"
              rf"b) CHF ${reduit}$" "\n\n"
              rf"${prix} - {prix * taux // 100} = {reduit}$, ou directement "
              rf"${prix} \cdot {(100-taux)/100:.2f}".replace(".", "{,}") + rf" = {reduit}$.")])


def relatifs(r):
    a, b = r.randint(12, 45), r.randint(15, 60)
    c, d = r.randint(3, 9), r.randint(4, 12)
    return (3, 1, "Nombres relatifs",
            "Calcule.",
            [("a", rf"$(-{a}) + (+{b}) - (-{c}) =$", rf"${-a + b + c}$" "\n\n"
              rf"$-{a} + {b} + {c} = {-a + b + c}$."),
             ("b", rf"$(-{c}) \cdot (+{d}) : (-{c}) =$", rf"${d}$" "\n\n"
              rf"$(-{c}) \cdot (+{d}) = -{c*d}$, puis $-{c*d} : (-{c}) = {d}$.")])


def vitesse(r):
    v = r.choice([60, 72, 80, 90, 96, 105, 120])
    h = r.choice([F(3,2), F(5,4), F(2), F(5,2), F(3,4)])
    dist = int(v * h)
    aff = f"{int(h)} h" if h.denominator == 1 else f"{int(h)} h {int((h - int(h)) * 60):02d}"
    if h < 1: aff = f"{int(h * 60)} minutes"
    return (3, 2, "Vitesse",
            "Calcule.",
            [("", rf"Un train parcourt ${dist}$ km en {aff}." "\n"
                  rf"a) Quelle est sa vitesse moyenne, en km/h ?" "\n"
                  rf"b) Quelle distance parcourrait-il en $3$ heures à cette vitesse ?",
              rf"a) ${v}$ km/h" "\n\n"
              rf"La vitesse est le quotient de la distance par la durée, exprimée en heures : "
              rf"${dist} : {str(h).replace('/', '/')} = {v}$." "\n\n"
              rf"b) ${v * 3}$ km" "\n\n" rf"${v} \cdot 3 = {v * 3}$.")])


def racines(r):
    c = r.choice([2, 3, 5, 6, 7])
    k = r.choice([2, 3, 4, 5, 6])
    car = r.choice([16, 25, 36, 49, 64, 81, 100, 121, 144])
    return (3, 1, "Racines carrées",
            "Calcule.",
            [("a", rf"$\sqrt{{{car}}} + \sqrt{{{k*k}}} =$", rf"${int(car**0.5) + k}$" "\n\n"
              rf"$\sqrt{{{car}}} = {int(car**0.5)}$ et $\sqrt{{{k*k}}} = {k}$."),
             ("b", rf"$\sqrt{{{c*c*k*k}}} =$", rf"${c*k}$" "\n\n"
              rf"${c*c*k*k} = {c*k}^2$, donc sa racine vaut ${c*k}$.")])


def solides(r):
    aire, h = r.randint(15, 48), r.randint(6, 18)
    return (3, 2, "Solides",
            "Calcule.",
            [("", rf"Un prisme droit a une aire de base de ${aire}$ "
                  rf"$\mathrm{{cm}}^2$ et une hauteur de ${h}$ cm." "\n"
                  rf"a) Calcule son volume." "\n"
                  rf"b) Combien de litres cela représente-t-il ?",
              rf"a) ${aire * h}$ $\mathrm{{cm}}^3$" "\n\n"
              rf"$V = \mathcal{{B}} \cdot h = {aire} \cdot {h} = {aire * h}$." "\n\n"
              rf"b) ${str(round(aire * h / 1000, 3)).replace('.', '{,}')}$ litre" "\n\n"
              rf"$1$ litre vaut $1000$ $\mathrm{{cm}}^3$.")])


# Les thèmes manquants, par section, dans l'ordre de leur fréquence réelle.
ROTATION = {
 "LS": [fractions, angles, pourcentages, relatifs],
 "LC": [vitesse, racines, solides],
 "CT": [pourcentages, vitesse, racines],
}


def ajouter(epreuve, niveau, variante, r):
    """Insère la question de complément à la fin de sa partie, puis renumérote."""
    fabrique = ROTATION[niveau][(variante - 1) % len(ROTATION[niveau])]
    points, partie, theme, consigne, sous = fabrique(r)
    nouvelle = _question(0, points, partie, theme, consigne, sous)

    questions = epreuve["questions"]
    dernier = max(i for i, q in enumerate(questions) if q["partie"] == partie)
    questions.insert(dernier + 1, nouvelle)
    for i, q in enumerate(questions, start=1):
        q["numero"] = i
    return epreuve
