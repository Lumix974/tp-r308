"""Créer une classe Personne avec les attributs : nom, age, salaire.
Ajouter une méthode afficher() et une méthode retraite(limite=62).
"""

# Création de la classe Personne
class Personne:

    # Constructeur de la classe
    def __init__(self, nom, age, salaire):

        # Initialisation des attributs de la personne
        self.nom = nom
        self.age = age
        self.salaire = salaire

    # Méthode permettant d'afficher les informations de la personne
    def afficher(self):
        print(self.nom)
        print(self.age)
        print(self.salaire)

    # Méthode permettant de vérifier si la personne peut partir à la retraite
    # La limite d'âge est de 62 ans par défaut
    def retraite(self, limite=62):

        # Vérifie si l'âge est supérieur ou égal à la limite
        if self.age >= limite:
            return "Retraite OK"
        else:
            return "Retraite pas OK"


# Ce bloc s'exécute uniquement si ce fichier est lancé directement
# Il ne s'exécute pas si la classe Personne est importée dans un autre fichier
if __name__ == "__main__":

    # Création d'un objet Personne
    p1 = Personne("Fabien", 65, 2000)

    # Affichage des informations de la personne
    p1.afficher()

    # Affichage du résultat de la méthode retraite()
    print(p1.retraite())