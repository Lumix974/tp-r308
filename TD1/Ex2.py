# Demande à l'utilisateur d'entrer un entier
n = int(input("Entrez un entier : "))

# Fonction qui calcule la somme des entiers de 1 jusqu'à n
def somme(n):

    # Variable qui va contenir la somme
    somme = 0

    # Boucle allant de 1 jusqu'à n inclus
    for i in range(1, n + 1):

        # Ajoute la valeur de i à la somme
        somme += i

    # Renvoie le résultat final
    return somme


# Appel de la fonction et affichage du résultat
print(somme(n))