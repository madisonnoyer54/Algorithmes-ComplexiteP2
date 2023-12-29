import random
import networkx as nx
import matplotlib.pyplot as plt


# On considère la capacité de chaque bin H = 150 dans tout le code 


# LECTURE FICHIER 
def lire_fichier(nom_fichier,nb):

    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
    

        ## Initialise
        list = [[] for _ in range(nb)]
     
        for ligne in lignes:
            # Vérifier que la ligne commence par 'e'
            if ligne.startswith('e'):
                try:
                    decomposeligne = ligne.split(" ")
                    list[int(decomposeligne[1])-1].append(int(decomposeligne[2]))
                except ValueError:
                    print(f"Erreur")

    return list

fichier_125 = lire_fichier("DSJC125.5.txt",125)
fichier_250 = lire_fichier("DSJC250.5.txt",250)
fichier_500 = lire_fichier("DSJC500.5.txt",500)
fichier_1000 = lire_fichier("DSJC1000.5.txt",1000)


# REMPLIR LES HAUTEURS
def remplirHauteurs(nb):
    objets = []
    h = 10
    sommet = 1

    quotient = nb // 41
    reste = nb % 41

    # Générer les poids en [10;50] uniformément 
    for i in range(41):
        for j in range(quotient):
            objets.append((sommet,h))
            sommet+=1
        h +=1

    # Paquet qui reste 
    for k in range(reste):
        h = random.randint(10, 50)
        objets.append((sommet,h))
        h +=1
        sommet+=1

    return objets

# QUESTION 1
def FractionalPacking(listObjets, tailleBoite):
    poidTotal = 0
    for objet in listObjets:
        poidTotal = objet[1] + poidTotal  # Récupérer le poids de l'objet

    quotient = poidTotal // tailleBoite
    reste = poidTotal % tailleBoite

    return quotient + (1 if reste != 0 else 0) # Rajoute 1 boite si il y a des reste 


## TESTE
print("Question 1")
# Exemple d'utilisation pour 125 
objets_125 = remplirHauteurs(125)

result = FractionalPacking(objets_125, 150)
print("Nombre de boîtes utilisées:", result)

# Exemple d'utilisation pour 250
objets_250 = remplirHauteurs(250)
result = FractionalPacking(objets_250, 150)
print("Nombre de boîtes utilisées:", result)

# Exemple d'utilisation pour 500
objets_500 = remplirHauteurs(500)
result = FractionalPacking(objets_500, 150)
print("Nombre de boîtes utilisées:", result) 

# Exemple d'utilisation pour 500
objets_1000 = remplirHauteurs(1000)
result = FractionalPacking(objets_1000, 150)
print("Nombre de boîtes utilisées:", result)



# Q2
# Fonction qui permet de gerer les conflit entre 2 sommet par rapport au fichier donner
def conflit(sommet1,sommet2,listObjets):
    confli = False 
  
    if len(listObjets) == 125:
        fichier = fichier_125
    elif len(listObjets) == 250:
        fichier = fichier_250
    elif len(listObjets) == 500: 
        fichier = fichier_500
    else:
        fichier = fichier_1000

    for i in fichier[sommet1-1]:
        if(i == sommet2):
            confli = True

    for i in fichier[sommet2-1]:
        if(i == sommet1):
            confli = True

    return confli



def FirstFitDecreasingPacking(listObjets, tailleBoite):
    # Remplissage : chaque liste représente une boîte avec [taille occupée, liste des couples (indice, taille) des objets dans la boîte]
    boites = []

    for objet in listObjets: 
        objetIndex, objetH = objet
        place = False

        i=0
        # Parcourir boite tanque boite pas trouver
        while i < len(boites) and place != True:
            conflit_present = False
            
            boite = boites[i]

            # Verif les conflits 
            for couple in boite[1]:
                if conflit(objetIndex, couple[0], listObjets): 
                    conflit_present = True
                    break

            # Si pas de conflit et la taille totale ne dépasse pas
            if not conflit_present and boite[0] + objetH <= tailleBoite: 
                boite[0] += objetH
                boite[1].append((objetIndex, objetH))
                place = True

                break

            i+=1

        # Si pas de place, créer boîte
        if not place:
            nouvelle_boite = [objetH, [(objetIndex, objetH)]] 
            boites.append(nouvelle_boite)

    return boites



## TESTE 

print("Question 2")
# Trie les objets par h décroissante
objetsTrie_125 = sorted(objets_125, key=lambda x: x[1], reverse=True)
remplissage = FirstFitDecreasingPacking(objetsTrie_125, 150)  
print(len(remplissage))

"""
for boite in remplissage:
    print(boite)
print()
"""

# Trie les objets par h décroissante
objetsTrie_250 = sorted(objets_250, key=lambda x: x[1], reverse=True)  
remplissage = FirstFitDecreasingPacking(objetsTrie_250, 150)

print(len(remplissage))
"""

for boite in remplissage:
    print(boite)

print()

"""

# Trie les objets par h décroissante
objetsTrie_500 = sorted(objets_500, key=lambda x: x[1], reverse=True)
remplissage = FirstFitDecreasingPacking(objetsTrie_500, 150)  

print(len(remplissage))
"""

for boite in remplissage:
    print(boite)

print()

"""

# Trie les objets par h décroissante
objetsTrie_1000 = sorted(objets_1000, key=lambda x: x[1], reverse=True) 
remplissage = FirstFitDecreasingPacking(objetsTrie_1000, 150)  
print(len(remplissage)) 

"""

for boite in remplissage:
    print(boite)

print()

"""


# QUESTION 3


def BestFitDecreasingPacking(listObjets, tailleBoite):
   # Remplissage : chaque liste represente une boite avec [taille occupée, liste des couples (indice, taille) des objets dans la boîte]
    boites = []

    for objet in listObjets: 
        objetIndex, objetH = objet 
        place = False

        # Trie boite en capaciter croissante ( logique car on l'ajoute a celle avec une + grand capacité )
        boites.sort(key=lambda x: x[0])
    
        i=0
        # Parcour les boite tanque boite pas trouver
        while i < len(boites) and place != True: 
            conflit_present = False
            
            boite = boites[i]

            # Verif les conflits 
            for couple in boite[1]: 
                if conflit(objetIndex, couple[0], listObjets):  
                    conflit_present = True
                    break

            # Si pas de conflit et la taille totale ne depasse pas
            if not conflit_present and boite[0] + objetH <= tailleBoite: 
                boite[0] += objetH
                boite[1].append((objetIndex, objetH))  
                place = True

                break

            i+=1
        # Si pas de place  cree boite
        if not place:
            nouvelle_boite = [objetH, [(objetIndex, objetH)]]
            boites.append(nouvelle_boite)

    return boites



print("QUESTION 3")
remplissage = BestFitDecreasingPacking(objetsTrie_125, 150)
print(len(remplissage))
"""
print(len(remplissage))

for boite in remplissage:
    print(boite)

print()
"""

remplissage = BestFitDecreasingPacking(objetsTrie_250, 150)
print(len(remplissage))
"""
print(len(remplissage))
for boite in remplissage:
    print(boite)

print()
"""


remplissage = BestFitDecreasingPacking(objetsTrie_500, 150)
print(len(remplissage))
"""
print(len(remplissage))
for boite in remplissage:
    print(boite)

print()
"""


remplissage = BestFitDecreasingPacking(objetsTrie_1000, 150)

print(len(remplissage))
"""
for boite in remplissage:
    print(boite)

print()
"""


## QUESTION 4
def Dsatur(graphe):
 
    couleurs = {} 
    sommetsRestants = set(graphe.keys()) # sommet pas encore colorer 
    degresSaturation = {v: 0 for v in graphe} 

    # sommet par ordre decroisse de degrès 
    sommetsTries = sorted(graphe.keys(), key=lambda x: len(graphe[x]), reverse=True) 

    # mettre sommet max a 1 
    sommet = sommetsTries[0]
    couleurs[sommet] = 1 
    sommetsRestants.remove(sommet)

    while sommetsRestants:
        # Choisir le sommet avec le degré de saturation maximal
        sommet = max(sommetsRestants, key=lambda x: (degresSaturation[x], len(graphe[x]))) 

        # Attribuer à sommet le numéro de couleur le plus petit possible
        couleursDisponibles = set(range(1, max(couleurs.values()) + 2))
        for voisin in graphe[sommet]:
            if voisin in couleurs: 
                couleursDisponibles.discard(couleurs[voisin])

        couleur = min(couleursDisponibles)
        couleurs[sommet] = couleur 
        sommetsRestants.remove(sommet) 

        # Mettre à jour les degrés de saturation des voisins
        for voisin in graphe[sommet]:
            degresSaturation[voisin] += 1  

    return couleurs  


# Permet de faire un graphe pas rapport au fichier et de l'afficher 
def afficherGrapheDsatur(fichier):
    # Crée graphe avec le fichier
    j = 1
    graphe = {}
    for i in fichier:
        graphe[j] = i
        j += 1


   # print(graphe)
    # Afficher
    G = nx.Graph(graphe)
    colors = Dsatur(graphe)

    node_colors = [colors[node] for node in G.nodes]
    pos = nx.spring_layout(G) 
    nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, cmap=plt.cm.rainbow)
    plt.show()

# Exemple 
#afficherGrapheDsatur(fichier_125)
#afficherGrapheDsatur(fichier_250)
#afficherGrapheDsatur(fichier_500)
#afficherGrapheDsatur(fichier_1000)

# Permet de mettre le poids sur le graphe color forme obtenu (index,poids,couleur)
def refaireGrapheAvecPoids(graphe,fichier):
    listTuple = []

    if len(graphe) == 125:
        objects = objets_125
    elif len(graphe) == 250:
        objects = objets_250
    elif len(graphe) == 500: 
        objects = objets_500
    else:
        objects = objets_1000
  
   
    for i in objects:
       j = i[0]
       listTuple.append((j,i[1],graphe[j]))


    return listTuple


# Permet de construire un graphe mais sens l'afficher 
def faireGraphe(fichier):
    j = 1
    graphe = {}
    for i in fichier:
        graphe[j] = i
        j += 1
    colors = Dsatur(graphe)

    return colors 


# Les differentes liste 
grapheColor_125 = refaireGrapheAvecPoids(faireGraphe(fichier_125),fichier_125)
grapheColor_250 = refaireGrapheAvecPoids(faireGraphe(fichier_250),fichier_250)
grapheColor_500 = refaireGrapheAvecPoids(faireGraphe(fichier_500),fichier_500)
grapheColor_1000 = refaireGrapheAvecPoids(faireGraphe(fichier_1000),fichier_1000)


"""
# Q5 
# Commes c'est colorer cette fois on utiliser les couleur pour les conflit 
def DsaturWithFFDpacking(tailleBoite, listObjets):
    # Remplissage : chaque liste représente une boîte avec [taille occupée, liste des couples (indice, taille) des objets dans la boîte]
    boites = []

    for objet in listObjets: 
   
        objetIndex, objetColor = objet
        place = False

        i=0
        # Parcourir boite tanque boite pas trouver
        while i < len(boites) and place != True:
            conflit_present = False
            
            boite = boites[i]

            # Verif les conflits 
            for couple in boite[1]:
                if couple[1] == objet[1]: 
                    conflit_present = True
                    break

            # Si pas de conflit et la taille totale ne dépasse pas
            if not conflit_present and boite[0] + objetColor <= tailleBoite: 
                boite[0] += objetColor
                boite[1].append((objetIndex, objetColor))
                place = True

                break

            i+=1

        # Si pas de place, créer boîte
        if not place:
            nouvelle_boite = [objetColor, [(objetIndex, objetColor)]] 
            boites.append(nouvelle_boite)

    return boites


def grapheCree(fichier):
    print(len(fichier))
    if len(fichier) == 125:
        h = objets_125
    elif len(fichier) == 250:
        h = objets_250
    elif len(fichier) == 500: 
        h = objets_500
    else:
        h = objets_1000


    # Crée graphe avec le fichier
    j = 0
    graphe = {}
    for i in fichier:
        graphe[h[j]] = i
        j += 1

    print(graphe)
    print("cc")
    colors = Dsatur(graphe)
    boites = DsaturWithFFDpacking(150,colors)
    print(len(boites))

grapheCree(fichier_125)

"""
exit()
