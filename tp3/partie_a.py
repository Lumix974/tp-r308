
class Livre:
    """
    Représente un livre pouvant être emprunté ou rendu.
    """

    def __init__(self, titre, auteur, annee):
        """
        Initialise un livre disponible.

        Paramètres :
            titre (str) : Titre du livre.
            auteur (str) : Auteur du livre.
            annee (int) : Année de publication.
        """
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.disponible = True  # Livre disponible par défaut
        self.emprunteur = None  # Aucun emprunteur initialement

    def afficher(self):
        """
        Affiche les informations et la disponibilité du livre.

        Retour :
            None
        """
        statut = "Disponible" if self.disponible else f"Emprunté par {self.emprunteur}"
        print(f"{self.titre} - {self.auteur} ({self.annee}) : {statut}")

    def emprunter(self, nom):
        """
        Permet d'emprunter un livre s'il est disponible.

        Paramètre :
            nom (str) : Nom de l'emprunteur.

        Retour :
            bool : True si l'emprunt réussit, sinon False.
        """
        if not self.disponible or not nom: return False  # Livre indisponible ou nom vide

        self.disponible = False  # Livre emprunté
        self.emprunteur = nom  # Enregistrement de l'emprunteur
        return True

    def rendre(self):
        """
        Rend un livre emprunté et le rend disponible.

        Retour :
            bool : True si le retour réussit, sinon False.
        """
        if self.disponible: return False  # Livre déjà disponible

        self.disponible = True  # Livre de nouveau disponible
        self.emprunteur = None  # Suppression de l'emprunteur
        return True


class Utilisateur:
    """
    Représente un utilisateur et ses livres empruntés.
    """

    def __init__(self, nom):
        """
        Initialise un utilisateur sans emprunt.

        Paramètre :
            nom (str) : Nom de l'utilisateur.
        """
        self.nom = nom
        self.emprunts = []  # Liste des livres empruntés

    def emprunter_livre(self, livre):
        """
        Permet à l'utilisateur d'emprunter un livre disponible.

        Paramètre :
            livre (Livre) : Livre à emprunter.

        Retour :
            bool : True si l'emprunt réussit, sinon False.
        """
        if not livre.emprunter(self.nom): return False  # Emprunt refusé

        self.emprunts.append(livre)  # Ajout à la liste des emprunts
        return True

    def rendre_livre(self, livre):
        """
        Permet à l'utilisateur de rendre un livre qu'il a emprunté.

        Paramètre :
            livre (Livre) : Livre à rendre.

        Retour :
            bool : True si le retour réussit, sinon False.
        """
        if livre not in self.emprunts or livre.emprunteur != self.nom:
            return False  # Livre non emprunté par cet utilisateur

        if not livre.rendre(): return False  # Retour impossible

        self.emprunts.remove(livre)  # Suppression de la liste
        return True

    def afficher_emprunts(self):
        """
        Affiche les livres empruntés par l'utilisateur.

        Retour :
            None
        """
        print(f"\nEmprunts de {self.nom} :")

        if not self.emprunts: print("Aucun livre emprunté.")

        for livre in self.emprunts:
            livre.afficher()  # Affichage des livres empruntés


# Tests du programme
if __name__ == "__main__":
    l = Livre("1984", "Orwell", 1949)  # Création du livre

    print("Premier emprunt :", l.emprunter("Ana"))
    print("Deuxième emprunt :", l.emprunter("Léo"))
    print("Retour :", l.rendre())

    ana = Utilisateur("Ana")  # Création d'un utilisateur

    print("\nEmprunt par Ana :", ana.emprunter_livre(l))
    ana.afficher_emprunts()

    print("\nRetour par Ana :", ana.rendre_livre(l))
    ana.afficher_emprunts()
