"""Écrire un programme qui demande à l’utilisateur 5 entiers et les stocke dans une liste.
Afficher le maximum, le minimum et la moyenne.
Trier la liste et l’afficher.
"""

# Création de la fonction qui va analyser la liste
def analyse_liste():

    # Création d'une liste vide
    liste = []

    # Boucle qui demande 5 entiers à l'utilisateur
    for i in range(5):

        # Récupération d'un entier
        n = int(input("Entrez un entier : "))

        # Ajout de l'entier dans la liste
        liste.append(n)

    # Affichage de la plus grande valeur
    print("Maximum :", max(liste))

    # Affichage de la plus petite valeur
    print("Minimum :", min(liste))

    # Calcul et affichage de la moyenne
    print("Moyenne :", sum(liste) / len(liste))

    # Tri de la liste dans l'ordre croissant
    liste.sort()

    # Affichage de la liste triée
    print("Liste triée :", liste)


# Appel de la fonction
analyse_liste()