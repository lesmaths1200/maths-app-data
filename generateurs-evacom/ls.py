# -*- coding: utf-8 -*-
"""EVACOM blanc, section 11LS : racines sous forme a√b, factorisation, volumes composés."""

def q(numero, points, partie, consigne, sous):
    return {"numero": numero, "points": points, "partie": partie, "consigne": consigne,
            "sousQuestions": [{"libelle": l, "enonce": e, "reponse": r} for l, e, r in sous]}

EPREUVE = {
    "id": "evacom-ls-1", "niveau": "LS", "titre": "EVACOM blanc n° 1 — section LS",
    "questions": [
        q(1, 5, 1, "Calcule et donne les réponses sous la forme d'une fraction irréductible ou d'un entier.", [
            ("a", r"$\sqrt{8} \cdot \sqrt{2} =$", r"$4$" "\n\n" r"$\sqrt{8} \cdot \sqrt{2} = \sqrt{16} = 4$."),
            ("b", r"$\frac{\sqrt{48}}{\sqrt{3}} =$", r"$4$" "\n\n" r"$\sqrt{\frac{48}{3}} = \sqrt{16} = 4$."),
            ("c", r"$(\sqrt{5} + 2)(\sqrt{5} - 2) =$", r"$1$" "\n\n"
             r"Identité remarquable : $(\sqrt{5})^2 - 2^2 = 5 - 4 = 1$."),
            ("d", r"$\frac{7}{12} + \frac{5}{18} =$", r"$\frac{31}{36}$" "\n\n"
             r"$\frac{21}{36} + \frac{10}{36} = \frac{31}{36}$."),
        ]),
        q(2, 3, 1, r"Écris sous la forme $a\sqrt{b}$, où $a$ est un entier et $b$ le plus petit possible.", [
            ("a", r"$\sqrt{50} =$", r"$5\sqrt{2}$" "\n\n" r"$50 = 25 \cdot 2$, donc $\sqrt{50} = \sqrt{25}\sqrt{2} = 5\sqrt{2}$."),
            ("b", r"$\sqrt{98} =$", r"$7\sqrt{2}$" "\n\n" r"$98 = 49 \cdot 2$, donc $\sqrt{98} = 7\sqrt{2}$."),
            ("c", r"$\sqrt{9 \cdot 12} =$", r"$6\sqrt{3}$" "\n\n"
             r"$9 \cdot 12 = 108 = 36 \cdot 3$, donc $\sqrt{108} = 6\sqrt{3}$."),
        ]),
        q(3, 3, 1, "Pour chaque item, coche la seule bonne réponse.", [
            ("a", r"$\sqrt{40}$ est compris entre :" "\n" r"$5$ et $6$  ·  $6$ et $7$  ·  $7$ et $8$",
             r"Entre $6$ et $7$" "\n\n" r"$6^2 = 36$ et $7^2 = 49$, or $36 < 40 < 49$."),
            ("b", r"$(-3)^4$ vaut :" "\n" r"$-81$  ·  $81$  ·  $-12$",
             r"$81$" "\n\n" r"L'exposant est pair, donc le résultat est positif."),
            ("c", r"$x^2 - 25$ se factorise en :" "\n" r"$(x-5)^2$  ·  $(x+5)(x-5)$  ·  $(x+25)(x-1)$",
             r"$(x+5)(x-5)$" "\n\n" r"C'est la différence de deux carrés."),
        ]),
        q(4, 3, 1, "Développe et réduis.", [
            ("a", r"$(2x - 3)^2 =$", r"$4x^2 - 12x + 9$" "\n\n" r"$(2x)^2 - 2 \cdot 2x \cdot 3 + 3^2$."),
            ("b", r"$(x + 4)(2x - 1) - 2x^2 =$", r"$7x - 4$" "\n\n"
             r"$(x+4)(2x-1) = 2x^2 - x + 8x - 4 = 2x^2 + 7x - 4$, puis on retranche $2x^2$."),
        ]),
        q(5, 7, 1, "Factorise au maximum.", [
            ("a", r"$9x^2 - 49 =$", r"$(3x+7)(3x-7)$" "\n\n" r"Différence de deux carrés : $(3x)^2 - 7^2$."),
            ("b", r"$5x^2 + 20x =$", r"$5x(x + 4)$" "\n\n" r"On met $5x$ en évidence."),
            ("c", r"$x^2 + 10x + 25 =$", r"$(x + 5)^2$" "\n\n" r"Carré parfait : $x^2 + 2 \cdot 5x + 5^2$."),
            ("d", r"$3x^2 - 27 =$", r"$3(x+3)(x-3)$" "\n\n"
             r"On met d'abord $3$ en évidence : $3(x^2 - 9)$, puis on factorise la différence de carrés."),
        ]),
        q(6, 2, 1, "Transforme la formule.", [
            ("", r"Le volume d'un cône est donné par $V = \frac{\pi r^2 h}{3}$." "\n"
                 r"Exprime la hauteur $h$ en fonction de $V$ et de $r$.",
             r"$h = \frac{3V}{\pi r^2}$" "\n\n"
             r"On multiplie les deux membres par $3$ : $3V = \pi r^2 h$, "
             r"puis on divise par $\pi r^2$."),
        ]),
        q(7, 4, 1, "Exprime l'aire à l'aide d'un polynôme réduit.", [
            ("", r"Un carré a pour côté $(x + 6)$. On y découpe, dans un coin, un carré de côté $x$ "
                 r"que l'on retire." "\n"
                 r"Exprime l'aire $A$ de la surface restante à l'aide d'un polynôme réduit.",
             r"$A = 12x + 36$" "\n\n"
             r"Grand carré : $(x+6)^2 = x^2 + 12x + 36$." "\n"
             r"Carré retiré : $x^2$." "\n"
             r"Différence : $x^2 + 12x + 36 - x^2 = 12x + 36$."),
        ]),
        q(8, 3, 2, "Résous le problème.", [
            ("", r"Un magicien demande à une spectatrice de penser à un nombre, d'y ajouter $7$, "
                 r"de multiplier le résultat par $3$, puis de retrancher le triple du nombre de départ." "\n"
                 r"Le magicien annonce le résultat sans rien demander. Quel est-il ? Justifie.",
             r"$21$, quel que soit le nombre choisi." "\n\n"
             r"Soit $n$ le nombre pensé." "\n"
             r"$3(n + 7) - 3n = 3n + 21 - 3n = 21$." "\n"
             r"Le nombre de départ disparaît : le résultat vaut toujours $21$."),
        ]),
        q(9, 3, 2, "Résous l'équation.", [
            ("", r"$\frac{2x - 1}{3} + 2 = \frac{x + 7}{2}$",
             r"$x = 11$" "\n\n"
             r"On multiplie tout par $6$ : $2(2x - 1) + 12 = 3(x + 7)$." "\n"
             r"$4x - 2 + 12 = 3x + 21$, donc $4x + 10 = 3x + 21$ et $x = 11$." "\n"
             r"Vérification : $\frac{21}{3} + 2 = 9$ et $\frac{18}{2} = 9$ ✓."),
        ]),
        q(10, 5, 2, "Identifie et calcule.", [
            ("a", r"Un solide a deux bases hexagonales identiques et parallèles, "
                  r"reliées par six faces rectangulaires. Quel est son nom ?",
             r"Un prisme droit à base hexagonale." "\n\n"
             r"Deux bases identiques et parallèles reliées par des rectangles caractérisent un prisme droit."),
            ("b", r"Son aire de base vaut $24$ cm$^2$ et sa hauteur $7$ cm. Calcule son volume.",
             r"$168$ cm$^3$" "\n\n" r"$V = \mathcal{B} \cdot h = 24 \cdot 7 = 168$."),
        ]),
        q(11, 6, 2, "Calcule et arrondis au centième.", [
            ("", r"Un solide est composé d'un cylindre de rayon $3$ cm et de hauteur $10$ cm, "
                 r"surmonté d'une demi-boule de même rayon." "\n"
                 r"Calcule son volume total en cm$^3$, arrondi au centième." "\n"
                 r"On rappelle que le volume d'une boule vaut $\frac{4\pi r^3}{3}$.",
             r"$339{,}29$ cm$^3$" "\n\n"
             r"Cylindre : $\pi \cdot 3^2 \cdot 10 = 90\pi$." "\n"
             r"Demi-boule : $\frac{1}{2} \cdot \frac{4\pi \cdot 27}{3} = 18\pi$." "\n"
             r"Total : $108\pi \approx 339{,}292$, soit $339{,}29$ cm$^3$."),
        ]),
        q(12, 4, 2, "Calcule et arrondis au dixième.", [
            ("", r"Un verre a la forme d'une pyramide à base carrée posée sur sa pointe. "
                 r"Le côté de sa base carrée mesure $6$ cm et sa hauteur $9$ cm." "\n"
                 r"a) Calcule le volume total du verre." "\n"
                 r"b) On le remplit de jus aux deux tiers de son volume. Quel volume de jus contient-il ?",
             r"a) $108$ cm$^3$" "\n\n" r"$V = \frac{\mathcal{B} \cdot h}{3} = \frac{36 \cdot 9}{3} = 108$." "\n\n"
             r"b) $72$ cm$^3$" "\n\n" r"$\frac{2}{3} \cdot 108 = 72$."),
        ]),
        q(13, 3, 2, "Justifie ta réponse.", [
            ("", r"$ABCD$ est un quadrilatère tel que $AB = 9$ cm, $BC = 40$ cm et la diagonale $AC = 41$ cm." "\n"
                 r"Le triangle $ABC$ est-il rectangle ? Si oui, en quel sommet ? Justifie.",
             r"Oui, rectangle en $B$." "\n\n"
             r"Le plus grand côté est $AC = 41$." "\n"
             r"$9^2 + 40^2 = 81 + 1600 = 1681$ et $41^2 = 1681$." "\n"
             r"Par la réciproque du théorème de Pythagore, le triangle est rectangle, "
             r"et l'angle droit est opposé à $[AC]$, donc en $B$."),
        ]),
    ],
}
