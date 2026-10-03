# -*- coding: utf-8 -*-
"""EVACOM blanc, section 11LC : calcul littéral, équations, Pythagore réciproque."""

def q(numero, points, partie, consigne, sous):
    return {"numero": numero, "points": points, "partie": partie, "consigne": consigne,
            "sousQuestions": [{"libelle": l, "enonce": e, "reponse": r} for l, e, r in sous]}

EPREUVE = {
    "id": "evacom-lc-1", "niveau": "LC", "titre": "EVACOM blanc n° 1 — section LC",
    "questions": [
        q(1, 6, 1, "Calcule et donne la réponse sous forme d'un entier ou d'une fraction irréductible.", [
            ("a", r"$\frac{5}{6} - \frac{3}{8} =$", r"$\frac{11}{24}$" "\n\n" r"$\frac{20}{24} - \frac{9}{24} = \frac{11}{24}$."),
            ("b", r"$\frac{14}{9} : \frac{7}{6} =$", r"$\frac{4}{3}$" "\n\n" r"$\frac{14}{9} \cdot \frac{6}{7} = \frac{84}{63} = \frac{4}{3}$."),
            ("c", r"$\frac{15}{8} \cdot \frac{12}{25} =$", r"$\frac{9}{10}$" "\n\n" r"$\frac{15 \cdot 12}{8 \cdot 25} = \frac{180}{200} = \frac{9}{10}$."),
            ("d", r"$49 : \sqrt{49} =$", r"$7$" "\n\n" r"$\sqrt{49} = 7$, et $49 : 7 = 7$."),
        ]),
        q(2, 4, 1, "Complète afin que chaque égalité soit vérifiée.", [
            ("a", r"$\frac{3}{4} + \frac{5}{8} + \frac{\square}{8} = 2$",
             r"$5$" "\n\n" r"$\frac{3}{4} = \frac{6}{8}$ et $2 = \frac{16}{8}$." "\n"
             r"Il manque donc $\frac{16}{8} - \frac{6}{8} - \frac{5}{8} = \frac{5}{8}$, soit $\square = 5$."),
            ("b", r"$\sqrt{\square} + 3 = 10$", r"$49$" "\n\n" r"$\sqrt{\square} = 7$, donc $\square = 49$."),
            ("c", r"$\frac{\square}{6} = \frac{10}{15}$", r"$4$" "\n\n" r"$\frac{10}{15} = \frac{2}{3} = \frac{4}{6}$."),
        ]),
        q(3, 2, 1, "Résous le problème.", [
            ("", r"Trois frères se partagent un héritage. L'État prélève d'abord le quart du total. "
                 r"Les trois frères se partagent équitablement ce qui reste et reçoivent CHF $12\,000$ chacun." "\n"
                 r"À combien s'élevait l'héritage au départ ?",
             r"CHF $48\,000$" "\n\n"
             r"Les trois frères reçoivent ensemble $3 \cdot 12\,000 = 36\,000$ CHF, "
             r"ce qui représente les $\frac{3}{4}$ de l'héritage." "\n"
             r"Le quart vaut donc $36\,000 : 3 = 12\,000$, et le total $12\,000 \cdot 4 = 48\,000$."),
        ]),
        q(4, 4, 1, "Complète afin que chaque égalité soit toujours vraie.", [
            ("a", r"$5x + 12 - (\square) = 2x$",
             r"$3x + 12$" "\n\n" r"$5x + 12 - (3x + 12) = 2x$."),
            ("b", r"$(x + 3)(x + \square) = x^2 + \square\,x + 12$",
             r"$4$ puis $7$" "\n\n" r"$(x+3)(x+4) = x^2 + 4x + 3x + 12 = x^2 + 7x + 12$."),
        ]),
        q(5, 2, 1, "Développe, puis donne la réponse sous forme réduite.", [
            ("", r"$(x - 5) + (3x + 2)(3x - 2) =$",
             r"$9x^2 + x - 9$" "\n\n"
             r"$(3x+2)(3x-2) = 9x^2 - 4$ (identité remarquable)." "\n"
             r"Donc $x - 5 + 9x^2 - 4 = 9x^2 + x - 9$."),
        ]),
        q(6, 3, 1, "Exprime l'aire à l'aide d'un polynôme réduit.", [
            ("", r"Un grand rectangle mesure $(2x + 5)$ de long et $x$ de large. "
                 r"On y découpe un carré de côté $x$, qu'on retire." "\n"
                 r"Exprime l'aire de la surface restante à l'aide d'un polynôme réduit.",
             r"$x^2 + 5x$" "\n\n"
             r"Aire du rectangle : $x(2x + 5) = 2x^2 + 5x$." "\n"
             r"Aire du carré : $x^2$." "\n"
             r"Différence : $2x^2 + 5x - x^2 = x^2 + 5x$."),
        ]),
        q(7, 2, 1, "Résous le problème.", [
            ("", r"Léa et Tom possèdent des billes. Léa dit à Tom : « Si tu me donnais $3$ billes, "
                 r"nous en aurions autant l'un que l'autre. »" "\n"
                 r"Tom répond : « Et si tu m'en donnais $3$, j'en aurais le double de toi. »" "\n"
                 r"Combien de billes chacun possède-t-il ?",
             r"Léa en a $15$, Tom en a $21$." "\n\n"
             r"Soit $\ell$ les billes de Léa et $t$ celles de Tom." "\n"
             r"Première phrase : $\ell + 3 = t - 3$, donc $t = \ell + 6$." "\n"
             r"Seconde phrase : $t + 3 = 2(\ell - 3)$." "\n"
             r"En substituant : $\ell + 9 = 2\ell - 6$, donc $\ell = 15$ et $t = 21$." "\n"
             r"Vérification : $15 + 3 = 18$ et $21 - 3 = 18$ ✓ ; $21 + 3 = 24 = 2 \cdot 12$ ✓."),
        ]),
        q(8, 2, 2, "Complète avec les mots qui conviennent.", [
            ("", "Mots proposés : hypoténuse  ·  cathètes  ·  rectangle  ·  isocèle  ·  réciproque\n\n"
                 "Si le carré du plus grand côté d'un triangle est égal à la somme des carrés des deux autres, "
                 "alors ce triangle est ______ . C'est la ______ du théorème de Pythagore.",
             "rectangle, puis réciproque\n\n"
             "La réciproque permet de démontrer qu'un triangle est rectangle à partir de ses seules longueurs."),
        ]),
        q(9, 2, 2, "Substitue puis calcule.", [
            ("", r"Substitue $a = 4$, $b = 2{,}5$ et $c = -3$ dans l'expression $2a + 4b - c$, puis calcule sa valeur.",
             r"$21$" "\n\n" r"$2 \cdot 4 + 4 \cdot 2{,}5 - (-3) = 8 + 10 + 3 = 21$."),
        ]),
        q(10, 4, 2, "Trouve la valeur de x.", [
            ("", r"Un rectangle a pour dimensions $(x + 2)$ et $6$. "
                 r"Un triangle équilatéral a un côté de $(2x)$." "\n"
                 r"Quelle doit être la valeur de $x$ pour que les deux figures aient le même périmètre ?",
             r"$x = 4$" "\n\n"
             r"Périmètre du rectangle : $2(x + 2) + 2 \cdot 6 = 2x + 16$." "\n"
             r"Périmètre du triangle : $3 \cdot 2x = 6x$." "\n"
             r"$2x + 16 = 6x$, donc $16 = 4x$ et $x = 4$." "\n"
             r"Vérification : rectangle $2 \cdot 6 + 12 = 24$ ; triangle $3 \cdot 8 = 24$ ✓."),
        ]),
        q(11, 2, 2, "Justifie ta réponse.", [
            ("", r"Une étagère est fixée contre un mur vertical. Elle avance de $24$ cm, "
                 r"son support descend de $32$ cm le long du mur, et la barre oblique qui relie "
                 r"les deux extrémités mesure $40$ cm." "\n"
                 r"L'étagère est-elle bien perpendiculaire au mur ? Justifie.",
             r"Oui." "\n\n"
             r"$24^2 + 32^2 = 576 + 1024 = 1600$ et $40^2 = 1600$." "\n"
             r"L'égalité de Pythagore est vérifiée : par la réciproque, le triangle est rectangle, "
             r"donc l'étagère est perpendiculaire au mur."),
        ]),
        q(12, 3, 2, "Justifie ta réponse.", [
            ("", r"Un triangle $ABC$ a pour côtés $AB = 20$ cm, $BC = 21$ cm et $AC = 29$ cm." "\n"
                 r"Ce triangle est-il rectangle ? Si oui, en quel sommet ?",
             r"Oui, rectangle en $B$." "\n\n"
             r"Le plus grand côté est $AC = 29$." "\n"
             r"$20^2 + 21^2 = 400 + 441 = 841$ et $29^2 = 841$." "\n"
             r"L'égalité est vérifiée, donc l'angle droit est opposé à $[AC]$, c'est-à-dire en $B$."),
        ]),
        q(13, 3, 2, "Calcule.", [
            ("", r"Un losange a une aire de $84$ cm$^2$ et sa grande diagonale mesure $14$ cm." "\n"
                 r"Calcule la longueur de sa petite diagonale.",
             r"$12$ cm" "\n\n"
             r"L'aire d'un losange vaut $\frac{D \cdot d}{2}$." "\n"
             r"$\frac{14 \cdot d}{2} = 84$, donc $7d = 84$ et $d = 12$."),
        ]),
        q(14, 4, 2, "Résous le problème.", [
            ("", r"Sarah investit une somme dans un projet. Le premier mois, elle perd le tiers de son "
                 r"investissement. Le deuxième mois, elle quadruple ce qui lui reste. "
                 r"Elle constate alors qu'elle possède CHF $1600$." "\n"
                 r"Combien avait-elle investi au départ ?",
             r"CHF $600$" "\n\n"
             r"Soit $x$ l'investissement de départ." "\n"
             r"Après le premier mois, il lui reste $\frac{2}{3}x$." "\n"
             r"Après le deuxième : $4 \cdot \frac{2}{3}x = \frac{8}{3}x = 1600$." "\n"
             r"Donc $x = 1600 \cdot \frac{3}{8} = 600$."),
        ]),
    ],
}
