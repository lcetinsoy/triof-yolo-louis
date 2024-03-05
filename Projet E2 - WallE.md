# Projet E2

Sujet d'amélioration d'une application d'IA.

Créateur : Louis Kuhn

## Contexte

Vous travaillez dans une société nommée Triof, qui veut faire du tri de déchêt plastiques automatique. 
Un précédente collaborateur a fait un proof of concept du system. 
On vous demande de le reprendre, de diagnostiquer ses erreurs et de l'améliorer. 

## Mission principale

Vous avez à votre disposition la petite application web dans le dossier `WallE-vision/`. Pour le moment, vous verrez que l'application est capable d'identifier certains objets dans les images mais elle n'est pas très douée sur les déchets....c'est votre mission : **vous devez reprendre l'application et l'améliorer afin qu'elle puisse détecter et identifier les déchets.**

N'ayant pas de données internes sur le sujet chez Triof, on vous suggère d'utiliser le jeu de données open source [TACO](http://tacodataset.org/) que vous pourrez récupérer en suivant à partir de [ce repo](https://github.com/pedropro/TACO).

Par ailleurs, même s'il n'est pas nécessaire de lire le papier scientifique sur le sujet, il vous faudra comprendre un peu comment fonctionne le modèle Yolo V7 dont vous trouverez une implémentation [ici](https://github.com/WongKinYiu/yolov7/).

## Missions annexes

Cela ne vous parlera pas tant que vous n'aurez mis un peu les mains dans le fonctionnement de l'application mais, si vous avez le temps, Triof s'est permis d'ajouter quelques idées d'améliorations possibles (facultatives et complémentaires !) :

1. gérer la prédiction d'une image à partir d'un autre stockage que local (une URL par exemple)
2. gérer le stockage de l'image prédite : pour le moment comment est-ce fait ? Quelle autre approche pourrait-on mettre en place ?
3. gérer l'inférence sur des vidéos
4. gérer l'inférence à partir de la webcam





