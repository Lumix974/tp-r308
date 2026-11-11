
from partie_a import Livre, Utilisateur


class Bibliotheque:
    """
    Représente une bibliothèque contenant des livres et des utilisateurs.
    """

    def __init__(self):
        """
        Initialise une bibliothèque vide.

        Retour :
            None
        """
        self.livres = {}  # Dictionnaire titre -> Livre
        self.utilisateurs = {}  # Dictionnaire nom -> Utilisateur

    def ajouter_livre(self, livre):
        """
        Ajoute un livre à la bibliothèque.

        Paramètre :
            livre (Livre) : Livre à ajouter.

        Retour :
            bool : True si l'ajout réussit, sinon False.
        """
        if livre.titre in self.livres:
            print("Erreur : ce livre existe déjà.")
            return False

        self.livres[livre.titre] = livre  # Enregistrement du livre
        return True

    def ajouter_utilisateur(self, utilisateur):
        """
        Ajoute un utilisateur à la bibliothèque.

        Paramètre :
            utilisateur (Utilisateur) : Utilisateur à inscrire.

        Retour :
            bool : True si l'ajout réussit, sinon False.
        """
        if utilisateur.nom in self.utilisateurs:
            print("Erreur : cet utilisateur existe déjà.")
            return False

        self.utilisateurs[utilisateur.nom] = utilisateur  # Enregistrement
        return True

    def emprunter(self, nom, titre):
        """
        Permet à un utilisateur d'emprunter un livre.

        Paramètres :
            nom (str) : Nom de l'utilisateur.
            titre (str) : Titre du livre.

        Retour :
            bool : True si l'emprunt réussit, sinon False.
        """
        if nom not in self.utilisateurs:
            print("Erreur : utilisateur inconnu.")
            return False

        if titre not in self.livres:
            print("Erreur : livre inconnu.")
            return False

        utilisateur = self.utilisateurs[nom]  # Recherche de l'utilisateur
        livre = self.livres[titre]  # Recherche du livre

        if not utilisateur.emprunter_livre(livre):
            print("Erreur : livre déjà emprunté.")
            return False

        print(f"{nom} a emprunté {titre}.")
        return True

    def rendre(self, nom, titre):
        """
        Permet à un utilisateur de rendre un livre.

        Paramètres :
            nom (str) : Nom de l'utilisateur.
            titre (str) : Titre du livre.

        Retour :
            bool : True si le retour réussit, sinon False.
        """
        if nom not in self.utilisateurs:
            print("Erreur : utilisateur inconnu.")
            return False

        if titre not in self.livres:
            print("Erreur : livre inconnu.")
            return False

        utilisateur = self.utilisateurs[nom]  # Recherche de l'utilisateur
        livre = self.livres[titre]  # Recherche du livre

        if not utilisateur.rendre_livre(livre):
            print("Erreur : ce livre n'a pas été emprunté par cet utilisateur.")
            return False

        print(f"{nom} a rendu {titre}.")
        return True

    def afficher_livres(self):
        """
        Affiche les livres disponibles et empruntés.

        Retour :
            None
        """
        if not self.livres:
            print("La bibliothèque est vide.")
            return

        print("\n--- Livres disponibles ---")

        for livre in self.livres.values():
            if livre.disponible: livre.afficher()  # Livres non empruntés

        print("\n--- Livres empruntés ---")

        for livre in self.livres.values():
            if not livre.disponible: livre.afficher()  # Livres empruntés


# Tests du programme
if __name__ == "__main__":
    b = Bibliotheque()  # Création de la bibliothèque

    b.ajouter_livre(Livre("1984", "Orwell", 1949))
    b.ajouter_livre(Livre("Dune", "Frank Herbert", 1965))
    b.ajouter_livre(Livre("Le Petit Prince", "Saint-Exupéry", 1943))

    b.ajouter_utilisateur(Utilisateur("Ana"))
    b.ajouter_utilisateur(Utilisateur("Léo"))

    print("\n--- Tests des emprunts ---")
    b.emprunter("Ana", "1984")
    b.emprunter("Léo", "Dune")

    b.afficher_livres()

    print("\n--- Tests des erreurs ---")
    b.emprunter("Léo", "1984")  # Livre déjà emprunté
    b.emprunter("Paul", "Dune")  # Utilisateur inconnu
    b.emprunter("Ana", "Inconnu")  # Livre inconnu
    b.rendre("Léo", "1984")  # Mauvais emprunteur

    print("\n--- Test du retour ---")
    b.rendre("Ana", "1984")

    b.afficher_livres()
