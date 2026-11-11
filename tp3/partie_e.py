
import json
from pathlib import Path
from partie_a import Livre, Utilisateur
from partie_b import Bibliotheque


def rechercher_auteur(bibliotheque, auteur):
    """
    Recherche les livres correspondant à un auteur.

    Paramètres :
        bibliotheque (Bibliotheque) : Bibliothèque à consulter.
        auteur (str) : Nom de l'auteur recherché.

    Retour :
        list : Liste des livres correspondants.
    """
    resultats = []  # Liste des livres trouvés

    if not auteur.strip(): return resultats  # Recherche vide

    for livre in bibliotheque.livres.values():
        if auteur.casefold() in livre.auteur.casefold():
            resultats.append(livre)  # Ajout du livre correspondant

    return resultats


def emprunter_limite(bibliotheque, nom, titre, limite=3):
    """
    Limite le nombre de livres empruntés par utilisateur.

    Paramètres :
        bibliotheque (Bibliotheque) : Bibliothèque à consulter.
        nom (str) : Nom de l'utilisateur.
        titre (str) : Titre du livre.
        limite (int) : Nombre maximal d'emprunts autorisés.

    Retour :
        bool : True si l'emprunt réussit, sinon False.
    """
    if nom in bibliotheque.utilisateurs:
        utilisateur = bibliotheque.utilisateurs[nom]

        if len(utilisateur.emprunts) >= limite:
            print(f"Erreur : limite de {limite} emprunts atteinte.")
            return False

    return bibliotheque.emprunter(nom, titre)  # Emprunt classique


def exporter_json(bibliotheque, fichier):
    """
    Exporte les livres et les utilisateurs au format JSON.

    Paramètres :
        bibliotheque (Bibliotheque) : Bibliothèque à exporter.
        fichier (str) : Chemin du fichier JSON.

    Retour :
        bool : True si l'export réussit, sinon False.
    """
    donnees = {
        "livres": [],
        "utilisateurs": list(bibliotheque.utilisateurs)
    }  # Structure des données

    for livre in bibliotheque.livres.values():
        donnees["livres"].append({
            "titre": livre.titre,
            "auteur": livre.auteur,
            "annee": livre.annee,
            "disponible": livre.disponible,
            "emprunteur": livre.emprunteur
        })  # Ajout des informations du livre

    try:
        with open(fichier, "w", encoding="utf-8") as f:
            json.dump(donnees, f, ensure_ascii=False, indent=4)

        print("Export JSON réalisé avec succès.")
        return True

    except (OSError, UnicodeError, TypeError) as e:
        print(f"Erreur d'export JSON : {e}")
        return False


# Tests du programme
if __name__ == "__main__":
    b = Bibliotheque()  # Création de la bibliothèque

    b.ajouter_utilisateur(Utilisateur("Ana"))

    b.ajouter_livre(Livre("1984", "George Orwell", 1949))
    b.ajouter_livre(Livre("La Ferme des animaux", "George Orwell", 1945))
    b.ajouter_livre(Livre("Dune", "Frank Herbert", 1965))
    b.ajouter_livre(Livre("Fondation", "Isaac Asimov", 1951))

    print("\n--- Recherche par auteur ---")

    for livre in rechercher_auteur(b, "orwell"):
        livre.afficher()

    print("\n--- Limite des emprunts ---")

    emprunter_limite(b, "Ana", "1984")
    emprunter_limite(b, "Ana", "Dune")
    emprunter_limite(b, "Ana", "Fondation")
    emprunter_limite(b, "Ana", "La Ferme des animaux")

    print("\n--- Export JSON ---")

    fichier = Path(__file__).with_name("bibliotheque.json")
    exporter_json(b, fichier)
