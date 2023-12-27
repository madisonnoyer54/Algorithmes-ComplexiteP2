import random

# On considère la capacité de chaque bin H = 150 dans tout le code 


# LECTURE FICHIER 
def lire_fichier(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        list = []

        for ligne in lignes:
            # Vérifier que la ligne commence par 'e'
            if ligne.startswith('e'):
                try:
                    
                    decomposeligne = ligne.split(" ")
                    list.append((int(decomposeligne[1]),int(decomposeligne[2])))
                except ValueError:
                    print(f"Erreur")

    return list

fichier_125 = lire_fichier("DSJC125.5.txt")
fichier_250 = lire_fichier("DSJC250.5.txt")
fichier_500 = lire_fichier("DSJC500.5.txt")
fichier_1000 = lire_fichier("DSJC1000.5.txt")


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
  
    if len(listObjets) == 125:
        fichier = fichier_125
    elif len(listObjets) == 250:
        fichier = fichier_250
    elif len(listObjets) == 500:
        fichier = fichier_500
    else:
        fichier = fichier_1000

    for arret in fichier:
        if((arret[0] == sommet1 and arret[1] == sommet2) or (arret[0] == sommet2 and arret[1] == sommet1)) :
            return True

    return False


def FirstFitDecreasingPacking(listObjets, tailleBoite):
    # Remplissage : chaque liste représente une boîte avec [taille occupée, liste des couples (indice, taille) des objets dans la boîte]
    boites = []

    for objet in listObjets: 
        objetIndex, objetH = objet
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


## TESTE 

print("Question 2")
# Trie les objets par poid décroissante
objetsTrie_125 = sorted(objets_125, key=lambda x: x[1], reverse=True)
remplissage = FirstFitDecreasingPacking(objetsTrie_125, 150)

"""
for boite in remplissage:
    print(boite)
print()
"""

# Trie les objets par poid décroissante
objetsTrie_250 = sorted(objets_250, key=lambda x: x[1], reverse=True)
remplissage = FirstFitDecreasingPacking(objetsTrie_250, 150)
"""

for boite in remplissage:
    print(boite)

print()

"""

# Trie les objets par poid décroissante
objetsTrie_500 = sorted(objets_500, key=lambda x: x[1], reverse=True)
remplissage = FirstFitDecreasingPacking(objetsTrie_250, 150)
"""

for boite in remplissage:
    print(boite)

print()

"""

# Trie les objets par poid décroissante
objetsTrie_1000 = sorted(objets_1000, key=lambda x: x[1], reverse=True)
remplissage = FirstFitDecreasingPacking(objetsTrie_250, 150)

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

        # Trie les boîtes par capacité restante croissante ( logique car on l'ajoute a celle avec une + grand capacité )
        boites.sort(key=lambda x: x[0])

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



print("QUESTION 3")
remplissage = BestFitDecreasingPacking(objetsTrie_125, 150)


for boite in remplissage:
    print(boite)

print()

remplissage = BestFitDecreasingPacking(objetsTrie_250, 150)

for boite in remplissage:
    print(boite)

print()


remplissage = BestFitDecreasingPacking(objetsTrie_500, 150)
for boite in remplissage:
    print(boite)

print()

remplissage = BestFitDecreasingPacking(objetsTrie_1000, 150)
for boite in remplissage:
    print(boite)

print()

