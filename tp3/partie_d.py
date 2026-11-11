import csv
from pathlib import Path
from partie_a import Livre, Utilisateur
from partie_c import sauvegarder_csv, charger_csv
from partie_e import rechercher_auteur, emprunter_limite, exporter_json


def sauvegarder_utilisateurs(bibliotheque, fichier):
    """
    Sauvegarde les utilisateurs dans un fichier CSV.

    Paramètres :
        bibliotheque (Bibliotheque) : Bibliothèque à sauvegarder.
        fichier (str) : Chemin du fichier CSV.

    Retour :
        bool : True si la sauvegarde réussit, sinon False.
    """
    try:
        with open(fichier, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nom"])  # En-tête du fichier

            for nom in bibliotheque.utilisateurs:
                writer.writerow([nom])  # Sauvegarde de l'utilisateur

        return True

    except (OSError, UnicodeError, csv.Error) as e:
        print(f"Erreur de sauvegarde des utilisateurs : {e}")
        return False


def charger_utilisateurs(bibliotheque, fichier):
    """
    Recharge les utilisateurs depuis un fichier CSV.

    Paramètres :
        bibliotheque (Bibliotheque) : Bibliothèque à compléter.
        fichier (str) : Chemin du fichier CSV.

    Retour :
        None
    """
    try:
        with open(fichier, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            if reader.fieldnames != ["nom"]:
                print("Erreur : fichier utilisateurs invalide.")
                return

            for ligne in reader:
                nom = ligne["nom"]

                if not nom or not nom.strip(): continue  # Nom vide ignoré

                nom = nom.strip()

                if nom not in bibliotheque.utilisateurs:
                    bibliotheque.ajouter_utilisateur(Utilisateur(nom))

    except FileNotFoundError:
        pass  # Premier lancement : aucun utilisateur enregistré

    except (OSError, UnicodeError, csv.Error, AttributeError) as e:
        print(f"Erreur de chargement des utilisateurs : {e}")


def afficher_menu():
    """
    Affiche le menu principal de la bibliothèque.

    Retour :
        None
    """
    print("\n--- Gestion de la bibliothèque ---")
    print("1 - Ajouter un livre")
    print("2 - Ajouter un utilisateur")
    print("3 - Emprunter un livre")
    print("4 - Rendre un livre")
    print("5 - Afficher les livres")
    print("6 - Rechercher un livre par auteur")
    print("7 - Exporter la bibliothèque en JSON")
    print("9 - Quitter et sauvegarder")


def jouer():
    """
    Lance le menu interactif de gestion de bibliothèque.

    Retour :
        None
    """
    fichier_livres = Path(__file__).with_name("livres.csv")
    fichier_utilisateurs = Path(__file__).with_name("utilisateurs.csv")

    b = charger_csv(fichier_livres)  # Chargement des livres
    charger_utilisateurs(b, fichier_utilisateurs)  # Chargement des utilisateurs

    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            titre = input("Titre du livre : ").strip()
            auteur = input("Auteur : ").strip()

            if not titre or not auteur:
                print("Erreur : titre ou auteur vide.")
                continue

            try:
                annee = int(input("Année de publication : "))
            except ValueError:
                print("Erreur : l'année doit être un entier.")
                continue

            livre = Livre(titre, auteur, annee)  # Création du livre

            if b.ajouter_livre(livre):
                print(f"Le livre {titre} a été ajouté.")

        elif choix == "2":
            nom = input("Nom de l'utilisateur : ").strip()

            if not nom:
                print("Erreur : nom vide.")
                continue

            utilisateur = Utilisateur(nom)  # Création de l'utilisateur

            if b.ajouter_utilisateur(utilisateur):
                print(f"L'utilisateur {nom} a été ajouté.")

        elif choix == "3":
            nom = input("Nom de l'utilisateur : ").strip()
            titre = input("Titre du livre : ").strip()

            emprunter_limite(b, nom, titre)  # Maximum de 3 livres

        elif choix == "4":
            nom = input("Nom de l'utilisateur : ").strip()
            titre = input("Titre du livre : ").strip()

            b.rendre(nom, titre)  # Tentative de retour

        elif choix == "5":
            b.afficher_livres()  # Affichage du catalogue

        elif choix == "6":
            auteur = input("Auteur recherché : ").strip()
            resultats = rechercher_auteur(b, auteur)

            if not resultats:
                print("Aucun livre trouvé.")
            else:
                print(f"\n{len(resultats)} livre(s) trouvé(s) :")

                for livre in resultats:
                    livre.afficher()

        elif choix == "7":
            fichier_json = Path(__file__).with_name("bibliotheque.json")
            exporter_json(b, fichier_json)  # Export des données

        elif choix == "9":
            livres_ok = sauvegarder_csv(b, fichier_livres)
            utilisateurs_ok = sauvegarder_utilisateurs(b, fichier_utilisateurs)

            if livres_ok and utilisateurs_ok:
                print("Bibliothèque sauvegardée. Au revoir !")
                break

            print("Erreur : sauvegarde incomplète.")

        else:
            print("Erreur : choix invalide.")


if __name__ == "__main__":
    jouer()  # Lancement du programme
