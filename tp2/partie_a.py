
class Grille:
    """
    Représente une grille de Morpion de 3 lignes et 3 colonnes.
    Les cases peuvent contenir "X", "O" ou un espace vide.
    """

    def __init__(self):
        """
        Initialise une grille vide de 3x3.

        Paramètres :
            Aucun.

        Retour :
            None
        """
        self.grille = [[" "] * 3 for _ in range(3)]  # Création de la grille


    def afficher(self):
        """
        Affiche la grille de Morpion dans le terminal.

        Paramètres :
            Aucun.

        Retour :
            None
        """
        for i, ligne in enumerate(self.grille):
            print(" | ".join(ligne))  # Affichage des cases

            if i < 2: print("---------")  # Séparation des lignes


    def jouer(self, x, y, joueur):
        """
        Place le symbole du joueur dans une case libre.

        Paramètres :
            x (int) : Numéro de ligne (0 à 2).
            y (int) : Numéro de colonne (0 à 2).
            joueur (str) : Symbole "X" ou "O".

        Retour :
            bool : True si le coup est valide, sinon False.
        """
        if joueur not in ("X", "O"):  # Vérification du symbole
            print("Erreur : le joueur doit être X ou O.")
            return False

        if not isinstance(x, int) or not isinstance(y, int) or not (0 <= x < 3 and 0 <= y < 3):
            print("Erreur : coordonnées hors grille.")
            return False

        if self.grille[x][y] != " ":  # Vérification de la case
            print("Erreur : case déjà occupée.")
            return False

        self.grille[x][y] = joueur  # Placement du symbole
        return True


    def est_gagnant(self, j):
        """
        Vérifie si un joueur a gagné sur une ligne, colonne ou diagonale.

        Paramètre :
            j (str) : Symbole du joueur ("X" ou "O").

        Retour :
            bool : True si le joueur a gagné, sinon False.
        """
        if j not in ("X", "O"): return False

        for i in range(3):
            if self.grille[i] == [j, j, j]: return True  # Ligne complète

            if self.grille[0][i] == self.grille[1][i] == self.grille[2][i] == j:
                return True  # Colonne complète

        if self.grille[0][0] == self.grille[1][1] == self.grille[2][2] == j:
            return True  # Diagonale principale

        if self.grille[0][2] == self.grille[1][1] == self.grille[2][0] == j:
            return True  # Diagonale secondaire

        return False


    def est_plein(self):
        """
        Vérifie si toutes les cases de la grille sont occupées.

        Paramètres :
            Aucun.

        Retour :
            bool : True si la grille est pleine, sinon False.
        """
        for ligne in self.grille:
            if " " in ligne: return False  # Case libre trouvée

        return True



if __name__ == "__main__":
    g = Grille()  # Création de la grille
    joueur = "X"  # Premier joueur

    print("Bienvenue dans le jeu du Morpion !")
    print("Entrez une ligne et une colonne entre 0 et 2.")

    while True:
        g.afficher()  # Affichage de la grille
        print(f"\nAu tour du joueur {joueur}")

        try:
            x = int(input("Ligne (0-2) : "))
            y = int(input("Colonne (0-2) : "))
        except ValueError:
            print("Erreur : entrez des entiers.")
            continue

        if not g.jouer(x, y, joueur): continue  # Coup invalide

        if g.est_gagnant(joueur):  # Vérification de la victoire
            g.afficher()
            print(f"Le joueur {joueur} a gagné !")
            break

        if g.est_plein():  # Vérification du match nul
            g.afficher()
            print("Match nul !")
            break

        joueur = "O" if joueur == "X" else "X"  # Changement de joueur

