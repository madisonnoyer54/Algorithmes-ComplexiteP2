import random
import networkx as nx
import matplotlib.pyplot as plt
print("Le programme peu mettre plusieurs minute du à la coloration des graphes")

# On considère la capacité de chaque bin H = 150 dans tout le code 

# Fonction qui permet d'afficher le detail des boites 
def afficheDetailBoite(remplissage):
    for boite in remplissage:
        print(boite)
    print()

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
test = lire_fichier("test1.txt",10)


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
#print("Question 1")
# Exemple d'utilisation pour 125 
objets_125 = remplirHauteurs(125)

remplissageQ1_125 = FractionalPacking(objets_125, 150)
#print("Borne inférieure pour 125:", remplissageQ1_125)

# Exemple d'utilisation pour 250
objets_250 = remplirHauteurs(250)
remplissageQ1_250 = FractionalPacking(objets_250, 150)
#print("Borne inférieure pour 250:", remplissageQ1_250)

# Exemple d'utilisation pour 500
objets_500 = remplirHauteurs(500)
remplissageQ1_500 = FractionalPacking(objets_500, 150)
#print("Borne inférieure pour 500:", remplissageQ1_500)

# Exemple d'utilisation pour 500
objets_1000 = remplirHauteurs(1000)
remplissageQ1_1000 = FractionalPacking(objets_1000, 150)
#print("Borne inférieure pour 1000:", remplissageQ1_1000)



# QUESTION 2
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
#print()
#print("Question 2")
# Trie les objets par h décroissante
objetsTrie_125 = sorted(objets_125, key=lambda x: x[1], reverse=True)
remplissageQ2_125 = FirstFitDecreasingPacking(objetsTrie_125, 150)  
#print("nombre de paquet utiliser pour 125:",len(remplissageQ2_125))
#afficheDetailBoite(remplissage)

# Trie les objets par h décroissante
objetsTrie_250 = sorted(objets_250, key=lambda x: x[1], reverse=True)  
remplissageQ2_250 = FirstFitDecreasingPacking(objetsTrie_250, 150)
#print("nombre de paquet utiliser pour 250:",len(remplissageQ2_250))
#afficheDetailBoite(remplissage)


# Trie les objets par h décroissante
objetsTrie_500 = sorted(objets_500, key=lambda x: x[1], reverse=True)
remplissageQ2_500 = FirstFitDecreasingPacking(objetsTrie_500, 150)  
#print("nombre de paquet utiliser pour 500:",len(remplissageQ2_500))
#afficheDetailBoite(remplissage)

# Trie les objets par h décroissante
objetsTrie_1000 = sorted(objets_1000, key=lambda x: x[1], reverse=True) 
remplissageQ2_1000 = FirstFitDecreasingPacking(objetsTrie_1000, 150)  
#print("nombre de paquet utiliser pour 1000:",len(remplissageQ2_1000))
#afficheDetailBoite(remplissage)



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


#print()
#print("QUESTION 3")
remplissageQ3_125 = BestFitDecreasingPacking(objetsTrie_125, 150)
#print("nombre de paquet utiliser pour 125:",len(remplissageQ3_125))
#afficheDetailBoite(remplissage)

remplissageQ3_250 = BestFitDecreasingPacking(objetsTrie_250, 150)
#print("nombre de paquet utiliser pour 250:",len(remplissageQ3_250))
#afficheDetailBoite(remplissage)



remplissageQ3_500 = BestFitDecreasingPacking(objetsTrie_500, 150)
#print("nombre de paquet utiliser pour 500:",len(remplissageQ3_500))
#afficheDetailBoite(remplissage)



remplissageQ3_1000 = BestFitDecreasingPacking(objetsTrie_1000, 150)
#print("nombre de paquet utiliser pour 1000:",len(remplissageQ3_1000))
#afficheDetailBoite(remplissage)



## QUESTION 4

def conflitGraphe(sommet, graph):
    liste = set(graph[sommet])

    for i in graph:
        for j in graph[i]:
            if j == sommet:
                liste.add(i)

    return list(liste)


def degresMaxColor(C,U,graph):
    conflitSup = U[0]
    compteMaxColor =0
    compteColor =0

    for j in U:
        conflitAvec = conflitGraphe(j,graph)
        for i in conflitAvec:
            if i in C:
                compteColor +=1
        
        # Si egale choisir degres max 
        if(compteColor == compteMaxColor):
            if(len(graph[j])>len(graph[conflitSup]) ):
                conflitSup = j

        # Prend le conflit conlorier sup
        if( compteColor > compteMaxColor):
            compteMaxColor = compteColor
            conflitSup = j


    return conflitSup




def Dsatur(graph):
    print("Commencement de la coloration du graphe: ",len(graph))
    #print("graphe ")
    couleurMax =0 # Couleur max possible
    couleurDispo ={0}
    # Etape 1
    # Initialisation
    U = set(graph.keys())  # Ensemble des sommets du graphe

    C = {}  # Ensemnble des sommet colorés 

    # Ordonner les sommets par ordre décroissant de degrés
    U = sorted(graph, key=lambda x: len(graph[x]), reverse=True)

    # Etape 2 
    v = U[0]
    C[v] = couleurMax
    U.remove(v)
   
 
    # Revenir a 3
    while len(C) != len(graph):
        print(C)
        # Couleur dispo sommet
        for i in range(couleurMax):
            couleurDispo.add(i)
            

        # Etape 3 
        v = degresMaxColor(C,U,graph)
      

        # Etape 4 
        # Trouver sa couleur
        conflitAvec = conflitGraphe(v,graph)

        # On deroule les sommet avec les conflit de v 
        for i in conflitAvec:
            if i in C and C[i] in couleurDispo:
         
                couleurDispo.remove(C[i])

   
        # Plus de couleur dispo 
        if(len(couleurDispo) == 0):
            #print("pas de couleur dispo")
            couleurMax+=1
            couleurDispo.add(couleurMax)
          
        
        C[v] = min(couleurDispo)
   
        U.remove(v)


    return C



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
#afficherGrapheDsatur(test)

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


# Les differentes liste avec les coloration 
grapheColor_125 = refaireGrapheAvecPoids(faireGraphe(fichier_125),fichier_125)
grapheColor_250 = refaireGrapheAvecPoids(faireGraphe(fichier_250),fichier_250)
grapheColor_500 = refaireGrapheAvecPoids(faireGraphe(fichier_500),fichier_500)
grapheColor_1000 = refaireGrapheAvecPoids(faireGraphe(fichier_1000),fichier_1000)
#grapheColor_10 = refaireGrapheAvecPoids(faireGraphe(test),test)



## QUESTION 5 
def DsaturWithFFDpacking(listObjets, tailleBoite):
    # Remplissage : chaque liste représente une boîte avec [taille occupée, liste des couples (indice, taille) des objets dans la boîte]
    boites = []

    for objet in listObjets: 
        objetIndex, objetH, objetC = objet
        place = False

        i=0
        # Parcourir boite tanque boite pas trouver
        while i < len(boites) and place != True:
            conflit_present = False
            
            boite = boites[i]

            # Verif les conflits 
            for couple in boite[1]:
                if objetC == couple[2]: 
                    conflit_present = True
                    break

            # Si pas de conflit et la taille totale ne dépasse pas
            if not conflit_present and boite[0] + objetH <= tailleBoite: 
                boite[0] += objetH
                boite[1].append((objetIndex, objetH,objetC))
                place = True

                break

            i+=1

        # Si pas de place, créer boîte
        if not place:
            nouvelle_boite = [objetH, [(objetIndex, objetH,objetC)]] 
            boites.append(nouvelle_boite)

    return boites

#print()
#print("QUESTION 5")
remplissageQ5_125 = DsaturWithFFDpacking(grapheColor_125,150)
#print("nombre de paquet utiliser pour 125:",len(remplissageQ5_125))
#afficheDetailBoite(remplissage)

remplissageQ5_250 = DsaturWithFFDpacking(grapheColor_250,150)
#print("nombre de paquet utiliser pour 250:",len(remplissageQ5_250))
#afficheDetailBoite(remplissage)

remplissageQ5_500 = DsaturWithFFDpacking(grapheColor_500,150)
#print("nombre de paquet utiliser pour 500:",len(remplissageQ5_500))
#afficheDetailBoite(remplissage)

remplissageQ5_1000 = DsaturWithFFDpacking(grapheColor_1000,150)
#print("nombre de paquet utiliser pour 1000:",len(remplissageQ5_1000))
#afficheDetailBoite(remplissage)


## QUESTION 6 
def DsaturWithBFDpacking(listObjets, tailleBoite):
   # Remplissage : chaque liste represente une boite avec [taille occupée, liste des couples (indice, taille) des objets dans la boîte]
    boites = []

    for objet in listObjets: 
        objetIndex, objetH, objetC = objet 
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
                if objetC == couple[2]:  
                    conflit_present = True
                    break

            # Si pas de conflit et la taille totale ne depasse pas
            if not conflit_present and boite[0] + objetH <= tailleBoite: 
                boite[0] += objetH
                boite[1].append((objetIndex, objetH,objetC))  
                place = True

                break

            i+=1
        # Si pas de place  cree boite
        if not place:
            nouvelle_boite = [objetH, [(objetIndex, objetH,objetC)]]
            boites.append(nouvelle_boite)

    return boites

#print()
#print("QUESTION 6")
remplissageQ6_125 = DsaturWithBFDpacking(grapheColor_125,150)
#print("nombre de paquet utiliser pour 125:",len(remplissageQ6_125))
#afficheDetailBoite(remplissage)

remplissageQ6_250 = DsaturWithBFDpacking(grapheColor_250,150)
#print("nombre de paquet utiliser pour 250:",len(remplissageQ6_250))
#afficheDetailBoite(remplissage)

remplissageQ6_500 = DsaturWithBFDpacking(grapheColor_500,150)
#print("nombre de paquet utiliser pour 500:",len(remplissageQ6_500))
#afficheDetailBoite(remplissage)

remplissageQ6_1000 = DsaturWithBFDpacking(grapheColor_1000,150)
#print("nombre de paquet utiliser pour 1000:",len(remplissageQ6_1000))
#afficheDetailBoite(remplissage)


## QUESTION 7

import matplotlib.pyplot as plt
import numpy as np

categories = ['125', '250', '500', '1000']
nombre_objets = [125, 250, 500, 1000]

# Borne inf
Q1 = [remplissageQ1_125, remplissageQ1_250, remplissageQ1_500, remplissageQ1_1000]
# FirstFitDecreasingPacking
Q2 = [len(remplissageQ2_125), len(remplissageQ2_250), len(remplissageQ2_500), len(remplissageQ2_1000)]
# BestFitDecreasingPacking 
Q3 = [len(remplissageQ3_125), len(remplissageQ3_250), len(remplissageQ3_500), len(remplissageQ3_1000)]
# DsaturWithFFDpacking
Q5 = [len(remplissageQ5_125), len(remplissageQ5_250), len(remplissageQ5_500), len(remplissageQ5_1000)]
# DsaturWithBFDpacking
Q6 = [len(remplissageQ6_125), len(remplissageQ6_250), len(remplissageQ6_500), len(remplissageQ6_1000)]

#### TABLEAU 
# Affichage du tableau
print("| {:<15} | {:<25} | {:<25} | {:<25} | {:<25} | {:<25} | ".format("Nombre d'objets", "Borne inférieur", "FirstFitDecreasingPacking", "BestFitDecreasingPacking", "DsaturWithFFDpacking", "DsaturWithBFDpacking"))
print("|" + "-"*17 + "|" + "-"*27 + "|" + "-"*27 + "|" + "-"*27 + "|" + "-"*27 + "|" + "-"*27 + "|")

for i in range(len(nombre_objets)):
    print("| {:<15} | {:<25} | {:<25} | {:<25} | {:<25} | {:<25} |".format(nombre_objets[i], Q1[i], Q2[i], Q3[i], Q5[i], Q6[i]))

### GRAPHE 
bar_width = 0.15  # Largeur des barres

fig, ax = plt.subplots(figsize=(10, 6))

bar_positions = np.arange(len(categories))

ax.bar(bar_positions - 2*bar_width, Q1, width=bar_width, label='Borne inférieure', color='yellow')
ax.bar(bar_positions - bar_width, Q2, width=bar_width, label='FirstFitDecreasingPacking', color='orange')
ax.bar(bar_positions, Q3, width=bar_width, label='BestFitDecreasingPacking', color='blue')
ax.bar(bar_positions + bar_width, Q5, width=bar_width, label='DsaturWithFFDpacking', color='green')
ax.bar(bar_positions + 2*bar_width, Q6, width=bar_width, label='DsaturWithBFDpacking', color='red')

ax.set_xticks(bar_positions)
ax.set_xticklabels(categories)
ax.set_xlabel('nombre d\'objets (125, 250, 500, 1000)')
ax.set_ylabel('Nombre de paquet')
ax.set_title('Comparaison entre les méthodes')
ax.legend()

plt.show()


exit()
