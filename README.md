# Données de l'app LesMaths1200

Dépôt public utilisé par l'app pour récupérer son contenu **sans avoir besoin
de republier l'app** : à chaque ouverture, l'app va chercher la version la
plus récente de ces fichiers ici, les met en cache, et retombe sur sa copie
embarquée si aucune connexion n'est disponible.

## Fichiers

- `cours.csv` — liste des cours/exercices (onglet Cours), avec le nom du
  fichier PDF correspondant (hébergé sur `lesmaths1200.github.io/cours/` ou
  `/exercices/`).
- `videos.csv` — les playlists YouTube (dossiers de l'onglet Vidéos).
- `playlist_videos.csv` — le détail de chaque playlist (Sujet, Exercice 1, 2…).
- `agenda.csv` — les événements de l'onglet Agenda.
- `chatbot.json` / `chatbot_taf.json` — les données de l'Assistant (thèmes,
  explications, exercices), au format utilisé par l'app (explications en
  tableau ordonné, pas en objet).

## Modifier le contenu

Éditer directement ces fichiers ici (respecter le séparateur `;` pour les
CSV) suffit : les élèves verront la mise à jour à la prochaine ouverture de
l'app, sans réinstallation.
