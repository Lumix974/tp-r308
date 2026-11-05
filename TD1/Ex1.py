# Demande à l'utilisateur de saisir deux entiers
a = int(input("1er entier : "))
b = int(input("2eme entier : "))


# Fonction qui retourne le plus petit des deux nombres
def petit(a, b):
    return f"Le plus petit nombre est {min(a, b)}"


# Fonction qui calcule et retourne la somme des deux nombres
def somme(a, b):
    return f"La somme de vos nombres est {a + b}"


# Fonction qui calcule le produit et indique s'il est pair ou impair
def produit(a, b):

    # Vérifie si le produit est divisible par 2
    if (a * b) % 2 == 0:
        return f"Le produit est pair : {a * b}"

    # Sinon, le produit est impair
    else:
        return f"Le produit est impair : {a * b}"


# Appel des fonctions et affichage des résultats
print(petit(a, b))
print(somme(a, b))
print(produit(a, b))