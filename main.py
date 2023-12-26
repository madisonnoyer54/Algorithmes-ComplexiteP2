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

    poid = 10
    # Paquet qui reste 
    for k in range(reste):
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

def FirstFitDecreasingPacking():
    return 3


def BestFitDecreasingPacking():
    return 4


# On considère la capacité de chaque bin H = 150
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







