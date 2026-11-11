from pathlib import Path
from tempfile import TemporaryDirectory

from partie_a import Livre, Utilisateur
from partie_b import Bibliotheque
from partie_c import charger_csv, sauvegarder_csv


def tester_bonus():
    """
    Vérifie les statistiques et les cas particuliers du TP3.

    Retour :
        None
    """
    b = Bibliotheque()  # Création de la bibliothèque

    b.ajouter_livre(Livre("1984", "Orwell", 1949))
    b.ajouter_livre(Livre("Dune", "Frank Herbert", 1965))
    b.ajouter_livre(Livre("Fondation", "Isaac Asimov", 1951))

    b.ajouter_utilisateur(Utilisateur("Ana"))
    b.ajouter_utilisateur(Utilisateur("Léo"))

    print("\n--- Tests des erreurs ---")

    assert b.emprunter("Ana", "Inconnu") is False  # Livre inconnu
    assert b.emprunter("Paul", "1984") is False  # Utilisateur inconnu

    assert b.emprunter("Ana", "1984") is True  # Premier emprunt
    assert b.emprunter("Léo", "1984") is False  # Livre déjà emprunté

    assert b.rendre("Léo", "1984") is False  # Mauvais emprunteur

    print("\n--- Test des statistiques ---")

    assert b.emprunter("Ana", "Dune") is True

    attendu = {
        "total": 3,
        "empruntes": 2,
        "par_utilisateur": {"Ana": 2}
    }

    assert b.stats() == attendu  # Vérification des statistiques
    print("Statistiques correctes :", b.stats())

    print("\n--- Test des fichiers CSV ---")

    with TemporaryDirectory() as dossier:
        fichier = Path(dossier) / "livres.csv"

        b_vide = charger_csv(fichier)  # Fichier absent
        assert b_vide.livres == {}

        assert sauvegarder_csv(b, fichier) is True

        b2 = charger_csv(fichier)  # Chargement des données

        assert b2.rendre("Léo", "1984") is False
        assert b2.rendre("Ana", "1984") is True

    print("\nTous les tests ont réussi !")


if __name__ == "__main__":
    tester_bonus()
