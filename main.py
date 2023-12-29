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
    sommet = 0

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
   # Remplissage : chaque liste représente une boîte avec [taille occupée, liste des couples (indice, taille) des objets dans la boîte]
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


def afficherGrapheDsatur(fichier):
    # Crée graphe avec le fichier
    j = 1
    graphe = {}
    for i in fichier:
        graphe[j] = i
        j += 1


    # Afficher
    G = nx.Graph(graphe)
    colors = Dsatur(graphe)
    node_colors = [colors[node] for node in G.nodes]
    pos = nx.spring_layout(G) 
    nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, cmap=plt.cm.rainbow)
    plt.show()

# Exemple 
afficherGrapheDsatur(fichier_125)
afficherGrapheDsatur(fichier_250)
afficherGrapheDsatur(fichier_500)
afficherGrapheDsatur(fichier_1000)

"""
def DsaturWithFFDpacking(listObjets, tailleBoite, colorationDsatur):
    # Remplissage : chaque liste représente une boîte avec [taille occupée, liste des couples (indice, taille) des objets dans la boîte]
    boites = []

    for objet in listObjets:
        objetIndex, objetH, couleur = objet
        place = False

        # Parcourir les boîtes existantes
        for boite in boites:
            conflit_present = False

            # Vérifier les conflits avec les objets déjà dans la boîte
            for couple in boite[1]:
                if conflit(objetIndex, couple[0], listObjets):
                    conflit_present = True
                    break

            # Si pas de conflit et la taille totale ne dépasse pas, placer l'objet dans la boîte
            if not conflit_present and boite[0] + objetH <= tailleBoite:
                boite[0] += objetH
                boite[1].append((objetIndex, objetH))
                place = True
                break

        # Si l'objet ne peut pas être placé dans une boîte existante, créer une nouvelle boîte
        if not place:
            nouvelle_boite = [objetH, [(objetIndex, objetH)]]
            boites.append(nouvelle_boite)

    return boites


def DsaturWithBFDpacking(listObjets, tailleBoite, colorationDsatur):
    # Remplissage : chaque liste représente une boîte avec [taille occupée, liste des couples (indice, taille) des objets dans la boîte]
    boites = []

    for objet in listObjets:
        objetIndex, objetH, couleur = objet
        place = False

        # Parcourir les boîtes existantes
        for boite in boites:
            conflit_present = False

            # Vérifier les conflits avec les objets déjà dans la boîte
            for couple in boite[1]:
                if conflit(objetIndex, couple[0], listObjets):
                    conflit_present = True
                    break

            # Si pas de conflit, calculer la capacité restante après insertion et placer l'objet dans la boîte avec la capacité la plus grande
            if not conflit_present:
                capacite_restante = tailleBoite - (boite[0] + objetH)
                if capacite_restante >= 0:
                    boite[0] += objetH
                    boite[1].append((objetIndex, objetH))
                    place = True
                    break

        # Si l'objet ne peut pas être placé dans une boîte existante, créer une nouvelle boîte
        if not place:
            nouvelle_boite = [objetH, [(objetIndex, objetH)]]
            boites.append(nouvelle_boite)

    return boites


# Définir les méthodes
methods = [FirstFitDecreasingPacking, BestFitDecreasingPacking, DsaturWithFFDpacking, DsaturWithBFDpacking]

# Définir le nombre d'objets
num_objects = [125, 250, 500, 1000]

# Stocker les résultats
results = {method.__name__: [] for method in methods}

# Générer des objets avec des tailles aléatoires
objects = [(i, random.randint(10, 50)) for i in range(1, max(num_objects) + 1)]

# Appliquer chaque méthode et stocker le nombre de boîtes utilisées
for method in methods:
    for n in num_objects:
        subset_objects = objects[:n]
        result = method(subset_objects, 150)  # Utiliser la taille de boîte appropriée
        num_boxes_used = len(result)
        results[method.__name__].append(num_boxes_used)

# Afficher les résultats
for method, result_list in results.items():
    print(f"{method}: {result_list}")

# Générer le graphique de comparaison
plt.figure(figsize=(10, 6))
for method, result_list in results.items():
    plt.plot(num_objects, result_list, label=method)

plt.xlabel("Nombre d'objets")
plt.ylabel("Nombre de boîtes utilisées")
plt.legend()
plt.title("Comparaison des méthodes par rapport à la borne inférieure")
plt.show()

"""

exit()
