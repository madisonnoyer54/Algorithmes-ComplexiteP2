import random


def remplirPoids(nb):
    objects = []
    poid = 10

    quotient = nb // 41
    reste = nb % 41

    # Générer les poids en [10;50] uniformément 
    for i in range(41):
        for j in range(quotient):
            objects.append((3,poid))
        poid = poid +1


    # Paquet qui reste 
    for k in range(reste):
        poid = random.randint(10, 50)
        objects.append((3,poid))
        poid = poid +1
   

    return objects

# Q1
def FractionalPacking(listObjets, tailleBoite):
    poidTotal = 0
    for object in listObjets:
        poidTotal = object[1] + poidTotal  # Récupérer le poids de l'objet

    quotient = poidTotal // tailleBoite
    reste = poidTotal % tailleBoite

    return quotient + (1 if reste != 0 else 0) # Rajoute 1 boite si il y a des reste 


# Q2
def FirstFitDecreasingPacking(listObjets, tailleBoite):
    listeTuples =[]

    return 3


def BestFitDecreasingPacking():
    return 4


# On considère la capacité de chaque bin H = 150

## QUESTION 1
# Exemple d'utilisation pour 125 
objects = remplirPoids(125)
result = FractionalPacking(objects, 150)
print("Nombre de boîtes utilisées:", result)

# Exemple d'utilisation pour 250
objects = remplirPoids(250)
result = FractionalPacking(objects, 150)
print("Nombre de boîtes utilisées:", result)

# Exemple d'utilisation pour 500
objects = remplirPoids(500)
result = FractionalPacking(objects, 150)
print("Nombre de boîtes utilisées:", result)

# Exemple d'utilisation pour 500
objects = remplirPoids(1000)
result = FractionalPacking(objects, 150)
print("Nombre de boîtes utilisées:", result)





## QUESTION 2 
def lire_fichier(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        list = []

        for ligne in lignes:
            # Vérifier que la ligne commence par 'e'
            if ligne.startswith('e'):
                try:
                    
                    decomposeligne = ligne.split(" ")
                    list.append((decomposeligne[1],decomposeligne[2]))
                except ValueError:
                    print(f"Erreur")

    return list
# Lire les objets à partir du fichier
list = lire_fichier("DSJC500.5.txt")


#print(list)


# Trie les objets par poid décroissante
sorted_objects = sorted(objects, key=lambda x: x[1], reverse=True)


