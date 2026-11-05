# Demande à l'utilisateur d'entrer un entier
n = int(input("Entrez un entier : "))


# Fonction qui calcule la somme des carrés de 1 jusqu'à n
def somme_carres(n):

    # Variable qui va contenir la somme
    somme = 0

    # Boucle allant de 1 jusqu'à n inclus
    for i in range(1, n + 1):

        # Ajoute le carré de i à la somme
        somme += i**2

    # Renvoie le résultat final
    return somme


# Appel de la fonction et affichage du résultat
print(somme_carres(n))