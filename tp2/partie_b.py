
import random
from partie_a import Grille


class JoueurHumain:
    """
    Représente un joueur humain qui choisit ses coups au clavier.
    """

    def prochain_coup(self, tab, symbole):
        """
        Demande au joueur de choisir une case libre.

        Paramètres :
            tab (list) : Grille du Morpion.
            symbole (str) : Symbole du joueur ("X" ou "O").

        Retour :
            tuple : Coordonnées (x, y) du coup choisi.
        """
        while True:
            try:
                print(f"\nAu tour du joueur {symbole}")
                x = int(input("Ligne (0-2) : "))
                y = int(input("Colonne (0-2) : "))

                if not (0 <= x < 3 and 0 <= y < 3):  # Vérification des coordonnées
                    print("Erreur : coordonnées hors grille.")
                    continue

                if tab[x][y] != " ":  # Vérification de la case
                    print("Erreur : case déjà occupée.")
                    continue

                return (x, y)  # Retourne le coup choisi

            except ValueError:  # Gestion des saisies invalides
                print("Erreur : entrez des entiers.")


class JoueurIA:
    """
    Représente un joueur IA qui choisit une case libre au hasard.
    """

    def prochain_coup(self, tab, symbole):
        """
        Choisit aléatoirement une case libre de la grille.

        Paramètres :
            tab (list) : Grille du Morpion.
            symbole (str) : Symbole du joueur ("X" ou "O").

        Retour :
            tuple : Coordonnées (x, y) du coup choisi.
            None : Si aucune case n'est disponible.
        """
        cases_libres = []  # Liste des cases disponibles

        for x in range(3):
            for y in range(3):
                if tab[x][y] == " ": cases_libres.append((x, y))

        return random.choice(cases_libres) if cases_libres else None


# Tests du programme
if __name__ == "__main__":
    g = Grille()  # Création de la grille

    humain = JoueurHumain()  # Création du joueur humain
    ia = JoueurIA()  # Création du joueur IA

    g.afficher()

    x, y = humain.prochain_coup(g.grille, "X")  # Coup humain
    g.jouer(x, y, "X")

    x, y = ia.prochain_coup(g.grille, "O")  # Coup de l'IA
    g.jouer(x, y, "O")

    print("\nGrille après les deux coups :")
    g.afficher()
