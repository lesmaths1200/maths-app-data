# -*- coding: utf-8 -*-
"""EVACOM blanc, section 11CT : relatifs, fractions, solides, Pythagore appliqué."""

def q(numero, points, partie, consigne, sous):
    return {"numero": numero, "points": points, "partie": partie,
            "consigne": consigne,
            "sousQuestions": [{"libelle": l, "enonce": e, "reponse": r} for l, e, r in sous]}

EPREUVE = {
    "id": "evacom-ct-1", "niveau": "CT", "titre": "EVACOM blanc n° 1 — section CT",
    "questions": [
        q(1, 4, 1, "Calcule.", [
            ("a", r"$(+42) + (-57) =$", r"$-15$" "\n\n" r"On retranche : $57 - 42 = 15$, et le plus grand nombre, $57$, est négatif."),
            ("b", r"$(+36) - (-14) =$", r"$50$" "\n\n" r"Soustraire un négatif revient à ajouter : $36 + 14 = 50$."),
            ("c", r"$(-6) \cdot (-9) =$", r"$54$" "\n\n" r"Deux facteurs négatifs donnent un produit positif."),
            ("d", r"$(-48) : (+6) =$", r"$-8$" "\n\n" r"Les signes sont différents, le quotient est négatif."),
        ]),
        q(2, 4, 1, "Calcule et donne la réponse sous forme d'une fraction irréductible.", [
            ("a", r"$\frac{8}{15} \cdot \frac{5}{12} =$",
             r"$\frac{2}{9}$" "\n\n" r"$\frac{8 \cdot 5}{15 \cdot 12} = \frac{40}{180} = \frac{2}{9}$."),
            ("b", r"$\frac{9}{14} : \frac{3}{7} =$",
             r"$\frac{3}{2}$" "\n\n" r"Diviser, c'est multiplier par l'inverse : $\frac{9}{14} \cdot \frac{7}{3} = \frac{63}{42} = \frac{3}{2}$."),
        ]),
        q(3, 3, 1, "Complète pour que chaque égalité soit vérifiée.", [
            ("a", r"$\frac{5}{12} + \frac{\square}{12} = \frac{11}{12}$",
             r"$6$" "\n\n" r"Les dénominateurs sont égaux : $11 - 5 = 6$."),
            ("b", r"$\frac{3}{4} \cdot \frac{\square}{5} = \frac{9}{20}$",
             r"$3$" "\n\n" r"$\frac{3 \cdot 3}{4 \cdot 5} = \frac{9}{20}$."),
            ("c", r"$\frac{7}{10} - \frac{\square}{5} = \frac{1}{10}$",
             r"$3$" "\n\n" r"$\frac{3}{5} = \frac{6}{10}$, et $\frac{7}{10} - \frac{6}{10} = \frac{1}{10}$."),
        ]),
        q(4, 4, 1, "Associe chaque solide à sa description. Écris le numéro de la description en face du solide.", [
            ("", "Solides : a) le cube  ·  b) le pavé droit  ·  c) le cylindre  ·  d) la pyramide à base carrée\n\n"
                 "Descriptions :\n"
                 "1. Deux bases circulaires identiques et parallèles, reliées par une surface courbe.\n"
                 "2. Six faces carrées.\n"
                 "3. Une base carrée et quatre faces triangulaires qui se rejoignent en un sommet.\n"
                 "4. Six faces rectangulaires, huit sommets et douze arêtes.",
             "a) 2  ·  b) 4  ·  c) 1  ·  d) 3\n\n"
             "Le cube est un pavé droit particulier : ses six faces sont des carrés."),
        ]),
        q(5, 3, 1, "Résous le problème.", [
            ("", r"Une bibliothèque compte $600$ livres. Les $\frac{3}{5}$ sont des romans. "
                 r"Parmi ces romans, $\frac{1}{4}$ sont des romans policiers." "\n"
                 r"a) Quelle fraction de tous les livres de la bibliothèque les romans policiers représentent-ils ?" "\n"
                 r"b) Combien y a-t-il de romans policiers ?",
             r"a) $\frac{3}{20}$" "\n\n" r"$\frac{3}{5} \cdot \frac{1}{4} = \frac{3}{20}$." "\n\n"
             r"b) $90$ romans policiers" "\n\n" r"$\frac{3}{20}$ de $600 = \frac{600}{20} \cdot 3 = 30 \cdot 3 = 90$."),
        ]),
        q(6, 4, 1, "Le théorème de Pythagore.", [
            ("a", "Complète : le théorème de Pythagore s'applique uniquement dans un triangle ______.",
             "rectangle\n\nIl relie les deux cathètes à l'hypoténuse d'un triangle rectangle."),
            ("b", r"Dans un triangle $ABC$ rectangle en $B$, coche la seule égalité correcte." "\n"
                  r"1. $AB^2 + BC^2 = AC^2$" "\n" r"2. $AB^2 + AC^2 = BC^2$" "\n" r"3. $AC^2 - BC^2 = AB^2 + BC^2$",
             r"La n° 1." "\n\n" r"L'angle droit est en $B$, donc l'hypoténuse est $[AC]$, le côté opposé : "
             r"la somme des carrés des cathètes $AB$ et $BC$ vaut $AC^2$."),
        ]),
        q(7, 3, 1, "Pour chaque grandeur, coche l'estimation la plus réaliste.", [
            ("a", "La hauteur d'une porte d'appartement : 0,2 m  ·  2 m  ·  20 m",
             r"$2$ m" "\n\n" r"$0{,}2$ m serait $20$ cm, et $20$ m la hauteur d'un immeuble."),
            ("b", "La contenance d'une canette de boisson : 3 dl  ·  3 l  ·  3 hl",
             r"$3$ dl" "\n\n" r"$3$ dl $= 0{,}3$ litre, soit $300$ ml."),
            ("c", "La masse d'une pomme : 15 g  ·  150 g  ·  1500 g",
             r"$150$ g" "\n\n" r"$1500$ g feraient $1{,}5$ kg, bien trop lourd pour une pomme."),
        ]),
        q(8, 2, 2, "Calcule et arrondis au dixième.", [
            ("", r"Un triangle rectangle a des cathètes de $9$ cm et $12$ cm. "
                 r"Calcule la longueur de son hypoténuse.",
             r"$15$ cm" "\n\n" r"$9^2 + 12^2 = 81 + 144 = 225$, et $\sqrt{225} = 15$."),
        ]),
        q(9, 4, 2, "Calcule.", [
            ("", r"Un rectangle a une diagonale de $13$ cm et une largeur de $5$ cm." "\n"
                 r"a) Calcule sa longueur." "\n" r"b) Calcule son aire.",
             r"a) $12$ cm" "\n\n" r"$13^2 - 5^2 = 169 - 25 = 144$, et $\sqrt{144} = 12$." "\n\n"
             r"b) $60$ cm$^2$" "\n\n" r"$12 \cdot 5 = 60$."),
        ]),
        q(10, 4, 2, "Compare et justifie.", [
            ("", r"Une voiture rouge parcourt $144$ km en $1$ h $30$. Une voiture verte parcourt $100$ km en $1$ h." "\n"
                 r"Quelle voiture roule le plus vite ? Justifie.",
             r"La voiture verte." "\n\n"
             r"Rouge : $144 : 1{,}5 = 96$ km/h. Verte : $100$ km/h." "\n"
             r"La verte roule donc plus vite, à $100$ km/h contre $96$ km/h."),
        ]),
        q(11, 3, 2, "Calcule et arrondis au dixième.", [
            ("", r"Calcule le volume d'un cylindre de rayon $5$ cm et de hauteur $12$ cm. "
                 r"Donne la réponse avec son unité.",
             r"$942{,}5$ cm$^3$" "\n\n"
             r"$V = \pi \cdot r^2 \cdot h = \pi \cdot 25 \cdot 12 = 300\pi \approx 942{,}48$, "
             r"soit $942{,}5$ cm$^3$ au dixième."),
        ]),
        q(12, 5, 2, "Choisis et justifie.", [
            ("", r"Un pâtissier dispose de deux moules." "\n"
                 r"Moule A : un cube d'arête $4$ cm." "\n"
                 r"Moule B : un pavé droit de $5$ cm, $4$ cm et $3$ cm." "\n"
                 r"Il veut fabriquer le plus grand nombre de gâteaux avec $3$ litres de pâte." "\n"
                 r"Quel moule doit-il choisir ? Justifie.",
             r"Le moule B." "\n\n"
             r"Moule A : $4^3 = 64$ cm$^3$. Moule B : $5 \cdot 4 \cdot 3 = 60$ cm$^3$." "\n"
             r"$3$ litres $= 3000$ cm$^3$." "\n"
             r"Avec A : $3000 : 64 = 46{,}875$, soit $46$ gâteaux." "\n"
             r"Avec B : $3000 : 60 = 50$ gâteaux." "\n"
             r"Le moule B, plus petit, permet donc d'en faire davantage."),
        ]),
        q(13, 3, 2, "Résous le problème.", [
            ("", r"Un bijoutier enfile $25$ perles cubiques de $8$ mm d'arête sur un fil. "
                 r"Il laisse $15$ mm de fil libre à chaque extrémité." "\n"
                 r"Quelle longueur de fil lui faut-il, en cm ?",
             r"$23$ cm" "\n\n"
             r"Perles : $25 \cdot 8 = 200$ mm. Fil libre : $2 \cdot 15 = 30$ mm." "\n"
             r"Total : $200 + 30 = 230$ mm $= 23$ cm."),
        ]),
    ],
}
