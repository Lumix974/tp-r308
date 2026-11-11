
from partie_b import JoueurIA


class JoueurIAMalin(JoueurIA):
    """
    Représente une IA qui cherche à gagner, puis à bloquer
    l'adversaire avant de jouer aléatoirement.
    """

    def coup_gagnant(self, tab, symbole):
        """
        Recherche un coup permettant de compléter une ligne gagnante.

        Paramètres :
            tab (list) : Grille du Morpion.
            symbole (str) : Symbole à rechercher.

        Retour :
            tuple : Coordonnées du coup gagnant, ou None.
        """
        combinaisons = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]  # Lignes, colonnes et diagonales

        for cases in combinaisons:
            valeurs = [tab[x][y] for x, y in cases]

            if valeurs.count(symbole) == 2 and valeurs.count(" ") == 1:
                return cases[valeurs.index(" ")]  # Case gagnante

        return None


    def prochain_coup(self, tab, symbole):
        """
        Choisit un coup gagnant, un blocage ou une case aléatoire.

        Paramètres :
            tab (list) : Grille du Morpion.
            symbole (str) : Symbole de l'IA.

        Retour :
            tuple : Coordonnées du coup choisi.
            None : Si aucune case n'est disponible.
        """
        coup = self.coup_gagnant(tab, symbole)  # Recherche d'une victoire
        if coup is not None: return coup

        adversaire = "O" if symbole == "X" else "X"
        coup = self.coup_gagnant(tab, adversaire)  # Recherche d'un blocage
        if coup is not None: return coup

        return super().prochain_coup(tab, symbole)  # Coup aléatoire


# Tests du programme
if __name__ == "__main__":
    ia = JoueurIAMalin()

    grille1 = [
        ["X", "X", " "],
        [" ", "O", " "],
        [" ", " ", " "]
    ]

    grille2 = [
        ["O", "O", " "],
        ["X", "X", " "],
        [" ", " ", " "]
    ]

    print("Blocage :", ia.prochain_coup(grille1, "O"))
    print("Victoire :", ia.prochain_coup(grille2, "O"))
