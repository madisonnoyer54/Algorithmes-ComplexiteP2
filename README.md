# Algorithmes-ComplexiteP2

## Desciption 
Projet réalisé en Master 1 Informatique dans le cadre de l'UE Algorithmes et Complexité.
Le code présenté est un projet de gestion de packing basé sur des algorithmes d’optimisation. Il utilise des structures de données comme des listes et des graphes pour organiser et traiter des objets (ou boîtes) en fonction de leur poids et de leurs contraintes de compatibilité.


Lancement du programme :
python3 main.py 


# Question 1 : 
Il a été nécessaire de mettre en place une fonction remplirHauteurs(nb) qui génère une liste de tuples (sommet, hauteur) afin d'uniformiser la hauteur de chaque boîte. Lorsque tous les sommets sont remplis de manière uniforme, les sommets restants sont complétés avec des hauteurs aléatoires entre 10 et 50. (Exemple : 41 * 3 + 2 = 125, donc 2 sommets sont remplis de manière aléatoire).

Par la suite, la fonction FractionalPacking a été implémentée comme demandé.

# Question 2 
Deux fonctions ont été mises en place pour permettre l'implémentation de la fonction FirstFitDecreasingPacking, conformément à la demande.

La fonction lire_fichier prend en paramètre le nom du fichier et le nombre de sommets présents. Elle retourne la liste des conflits présents dans chaque fichier. (Exemple fichier 125 : list[4-1] = [1, 2, 3], indiquant que le sommet 4 est en conflit avec les sommets 1, 2 et 3.)

La fonction conflit prend en paramètre deux sommets, sommet1 et sommet2, ainsi qu'une liste d'objets. Elle sélectionne le fichier correspondant en fonction de la taille de la liste donnée, puis examine les conflits entre les deux sommets. Elle retourne True s'il y a un conflit, sinon False.

La fonction FirstFitDecreasingPacking a été mise en œuvre conformément à l'énoncé.

# Question 3 
La fonction BestFitDecreasingPacking a été implémentée selon les instructions de l'énoncé en utilisant la fonction conflit décrite précédemment.

Les Questions 2 et 3 ont été testées avec la fonction afficheDetailBoite(remplissage), qui permet d'afficher en détail les boîtes obtenues. Les lignes en commentaire vont de 241 à 258 et de 172 à 195.

# Question 4 
Pour cette question, deux fonctions supplémentaires ont été créées.

La fonction conflitGraphe prend en paramètre un sommet et le graphe, et retourne la liste des conflits du sommet.

La fonction degresMaxColor prend en paramètre la liste des sommets coloriés, la liste des sommets restants et le graphe. Elle retourne le sommet qui a le plus de voisins coloriés. En cas d'égalité, le sommet avec le plus grand nombre de degrés est retenu.

Ensuite, la fonction Dsatur a été implémentée conformément aux directives.

Enfin, cette fonction a été testée grâce à la création d'un graphe. Une fonction afficherGrapheDsatur a été élaborée pour prendre le fichier en paramètre, créer un graphe à partir de celui-ci, appliquer la fonction Dsatur et afficher le résultat graphiquement.

Des fichiers plus petits ont été créés pour faciliter l'affichage et rendre les tests plus lisibles. (Exemple : GrapheFichierTest.png, montrant le graphe colorié à partir du fichier test1.txt. GrapheFichier125.png, montrant le graphe colorié à partir du fichier DSJC125.5.txt.)

Pour afficher les graphes sur votre machine, il suffit d'enlever les commentaires des lignes 378 à 382.

# Question 5 
Deux fonctions ont été élaborées pour la mise en œuvre de la Question 5.

La fonction faireGraphe prend en paramètre le fichier et retourne le graphe colorié correspondant.

La fonction refaireGrapheAvecPoids prend le graphe colorié et retourne une liste de tuples (index, hauteur, couleur).

La fonction DsaturWithFFDpacking a été implémentée comme demandé dans l'énoncé.

# Question 6 
Grâce aux fonctions implémentées pour la question 5, la fonction a été réalisée conformément aux instructions de l'énoncé.

# Question 7
Grâce aux imports matplotlib.pyplot as plt et import numpy as np, un graphique en bâton a été créé pour comparer les différentes fonctions implémentées ci-dessus. (Voir GrapheFinal.png)

Un récapitulatif sous forme de tableau s'affiche dans le terminal. (Voir TableauFinal.png)


Conclusion :
Je tiens à préciser que la création des graphes peut prendre plusieurs minutes, surtout la coloration pour le graphe à 1000 sommets. Les questions Q5 et Q6 montrent des résultats moins et nécessitent plus de temps en comparaison avec Q2 et Q3 (cause : coloration). Pour les Q5 et Q6, les paquet sont crée grâce au couleur des sommets. Si il ont la même couleur il n'ont pas de conflit.


