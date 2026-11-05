"""Créer une classe Employe héritant de Personne, avec un attribut prime.
Redéfinir la méthode afficher().
Tester avec plusieurs employés dans une liste.
"""

# Importation de la classe Personne depuis le fichier Ex7.py
from Ex7 import Personne

# Création de la classe Employe qui hérite de la classe Personne
class Employe(Personne):

    # Constructeur de la classe Employe
    def __init__(self, nom, age, salaire, prime):

        # Appel du constructeur de la classe Personne
        # pour initialiser le nom, l'âge et le salaire
        super().__init__(nom, age, salaire)

        # Initialisation de l'attribut prime propre à Employe
        self.prime = prime

    # Redéfinition de la méthode afficher()
    def afficher(self):

        # Appel de la méthode afficher() de la classe Personne
        # pour afficher le nom, l'âge et le salaire
        super().afficher()

        # Affichage de la prime de l'employé
        print(self.prime)


# Création de deux objets Employe
e1 = Employe("Fabien", 25, 2000, 300)
e2 = Employe("Lucas", 30, 2300, 400)

# Stockage des employés dans une liste
employes = [e1, e2]

# Parcours de la liste pour afficher les informations de chaque employé
for employe in employes:
    employe.afficher()