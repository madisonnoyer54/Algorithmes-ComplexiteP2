import random


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

def remplirPoids(nb):
    objects = []
    poid = 10
    sommet = 0

    quotient = nb // 41
    reste = nb % 41

    # Générer les poids en [10;50] uniformément 
    for i in range(41):
        for j in range(quotient):
            objects.append((sommet,poid))
            sommet=sommet+1
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
    

    return 3


def BestFitDecreasingPacking():
    return 4


# On considère la capacité de chaque bin H = 150


## QUESTION 1
print("Question 1")
# Exemple d'utilisation pour 125 
objects_125 = remplirPoids(125)
result = FractionalPacking(objects_125, 150)
print("Nombre de boîtes utilisées:", result)

# Exemple d'utilisation pour 250
objects_250 = remplirPoids(250)
result = FractionalPacking(objects_250, 150)
print("Nombre de boîtes utilisées:", result)

# Exemple d'utilisation pour 500
objects_500 = remplirPoids(500)
result = FractionalPacking(objects_500, 150)
print("Nombre de boîtes utilisées:", result)

# Exemple d'utilisation pour 500
objects_1000 = remplirPoids(1000)
result = FractionalPacking(objects_1000, 150)
print("Nombre de boîtes utilisées:", result)





## QUESTION 2 
# Lire les objets à partir du fichier
listFichier_125 = lire_fichier("DSJC125.5.txt")
listFichier_250 = lire_fichier("DSJC250.5.txt")
listFichier_500 = lire_fichier("DSJC500.5.txt")
listFichier_1000 = lire_fichier("DSJC1000.5.txt")



print("Question 2")
# Trie les objets par poid décroissante
objectsTrie_125 = sorted(objects_125, key=lambda x: x[1], reverse=True)
remplissage = FirstFitDecreasingPacking(objectsTrie_125, 150)

# Trie les objets par poid décroissante
objectsTrie_250 = sorted(objects_250, key=lambda x: x[1], reverse=True)
remplissage = FirstFitDecreasingPacking(objectsTrie_250, 150)

# Trie les objets par poid décroissante
objectsTrie_500 = sorted(objects_500, key=lambda x: x[1], reverse=True)
remplissage = FirstFitDecreasingPacking(objectsTrie_250, 150)

# Trie les objets par poid décroissante
objectsTrie_1000 = sorted(objects_1000, key=lambda x: x[1], reverse=True)
remplissage = FirstFitDecreasingPacking(objectsTrie_250, 150)
