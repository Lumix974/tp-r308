
import csv
from pathlib import Path
from partie_a import Livre, Utilisateur
from partie_b import Bibliotheque


def sauvegarder_csv(bibliotheque, fichier):
    """
    Sauvegarde les livres et leurs emprunts dans un fichier CSV.

    Paramètres :
        bibliotheque (Bibliotheque) : Bibliothèque à sauvegarder.
        fichier (str) : Chemin du fichier CSV.

    Retour :
        bool : True si la sauvegarde réussit, sinon False.
    """
    try:
        with open(fichier, "w", newline="", encoding="utf-8") as f:
            colonnes = ["titre", "auteur", "annee", "disponible", "emprunteur"]
            writer = csv.DictWriter(f, fieldnames=colonnes)

            writer.writeheader()  # Écriture des noms des colonnes

            for livre in bibliotheque.livres.values():
                writer.writerow({
                    "titre": livre.titre,
                    "auteur": livre.auteur,
                    "annee": livre.annee,
                    "disponible": livre.disponible,
                    "emprunteur": livre.emprunteur or ""
                })  # Sauvegarde du livre

        return True

    except (OSError, UnicodeError, csv.Error) as e:
        print(f"Erreur de sauvegarde : {e}")
        return False


def charger_csv(fichier):
    """
    Charge les livres et leurs emprunts depuis un fichier CSV.

    Paramètre :
        fichier (str) : Chemin du fichier CSV.

    Retour :
        Bibliotheque : Bibliothèque contenant les données chargées.
    """
    bibliotheque = Bibliotheque()  # Nouvelle bibliothèque

    try:
        with open(fichier, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            colonnes = ["titre", "auteur", "annee", "disponible", "emprunteur"]

            if reader.fieldnames != colonnes:
                print("Erreur : colonnes CSV invalides.")
                return bibliotheque

            for numero, ligne in enumerate(reader, start=2):
                try:
                    titre = ligne["titre"].strip()
                    auteur = ligne["auteur"].strip()
                    annee = int(ligne["annee"])
                    disponible = ligne["disponible"].strip().lower()
                    emprunteur = ligne["emprunteur"].strip()

                except (ValueError, AttributeError):
                    print(f"Ligne {numero} invalide.")
                    continue

                if not titre or not auteur or disponible not in ("true", "false"):
                    print(f"Ligne {numero} invalide.")
                    continue

                if (disponible == "true" and emprunteur) or (disponible == "false" and not emprunteur):
                    print(f"Ligne {numero} incohérente.")
                    continue

                livre = Livre(titre, auteur, annee)  # Recréation du livre

                if not bibliotheque.ajouter_livre(livre):
                    continue

                if disponible == "false":
                    if emprunteur not in bibliotheque.utilisateurs:
                        bibliotheque.ajouter_utilisateur(Utilisateur(emprunteur))

                    utilisateur = bibliotheque.utilisateurs[emprunteur]
                    utilisateur.emprunter_livre(livre)  # Restauration de l'emprunt

    except FileNotFoundError:
        print("Fichier absent : bibliothèque vide.")

    except (OSError, UnicodeError, csv.Error) as e:
        print(f"Erreur de chargement : {e}")

    return bibliotheque


# Tests du programme
if __name__ == "__main__":
    fichier = Path(__file__).with_name("livres.csv")  # Chemin de sauvegarde

    b = Bibliotheque()  # Création de la bibliothèque

    b.ajouter_livre(Livre("1984", "Orwell", 1949))
    b.ajouter_livre(Livre("Dune", "Frank Herbert", 1965))
    b.ajouter_utilisateur(Utilisateur("Ana"))

    b.emprunter("Ana", "1984")  # Emprunt avant sauvegarde

    if sauvegarder_csv(b, fichier):
        print("\nBibliothèque sauvegardée.")

        b2 = charger_csv(fichier)  # Rechargement dans une autre bibliothèque

        print("\n--- Livres rechargés ---")
        b2.afficher_livres()

        print("\n--- Test du retour après rechargement ---")
        print("Retour réussi :", b2.rendre("Ana", "1984"))

        b2.afficher_livres()
