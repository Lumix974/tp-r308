import math
from pathlib import Path
from partie_c import mots, choisir_mot, masque

def jouer_pendu(mot):
    """
    Lance une partie du Pendu avec un maximum de 7 erreurs.

    Paramètres :
        mot (str) : Mot que le joueur doit deviner.

    Retour :
        str : Message de victoire ou de défaite.
    """
    mot = mot.upper()  # Conversion en majuscules
    mot_masque = masque(mot)  # Création du masque
    erreurs = 0  # Compteur d'erreurs
    lettres_proposees = []  # Historique des lettres

    dessins = [
        "",
        " O",
        " O\n |",
        " O\n/|",
        " O\n/|\\",
        " O\n/|\\\n/",
        " O\n/|\\\n/ \\",
        " |----\n O\n/|\\\n/ \\"
    ]  # Dessins correspondant aux 0 à 7 erreurs

    print("\nBienvenue dans le jeu du Pendu !")

    while erreurs < 7 and "_" in mot_masque:  # Conditions de fin du jeu
        print("\nMot :", " ".join(mot_masque))  # Affichage du mot masqué
        print(f"Erreurs : {erreurs}/7")  # Affichage des erreurs
        print("Lettres proposées :", ", ".join(lettres_proposees))
        print(dessins[erreurs])  # Affichage du pendu

        lettre = input("Proposez une lettre : ").strip().upper()

        if len(lettre) != 1 or not lettre.isalpha():  # Vérification de la saisie
            print("Erreur : entrez une seule lettre.")
            continue

        if lettre in lettres_proposees:  # Vérification des doublons
            print("Cette lettre a déjà été proposée.")
            continue

        lettres_proposees.append(lettre)  # Enregistrement de la lettre

        if lettre in mot:
            for i, caractere in enumerate(mot):  # Parcours du mot
                if caractere == lettre:
                    mot_masque[i] = lettre  # Révélation de la lettre

            print("Bonne lettre !")
        else:
            erreurs += 1  # Incrémentation des erreurs
            print("Mauvaise lettre !")

    print("\nMot :", " ".join(mot_masque))
    print(f"Erreurs : {erreurs}/7")
    print(dessins[erreurs])

    resultat = "Gagné" if "_" not in mot_masque else "Perdu"
    return f"{resultat} ! Le mot était {mot}."

def choisir_mode():
    """
    Permet de choisir entre le mode solo et le mode deux joueurs.

    Retour :
        str : Mot à deviner en majuscules.
        None : Si aucun mot n'est disponible.
    """
    while True:
        print("\n1 - Jouer seul\n2 - Jouer à deux")

        choix = input("Choisissez un mode (1/2) : ").strip()

        if choix == "1": return choisir_mot(mots)  # Mode solo, Mot aléatoire de la partie C

        if choix == "2":
            while True:
                mot = input("Joueur 1, entrez un mot : ").strip().upper()

                if mot.isalpha():  # Vérification du mot
                    print("\n" * 40)  # Masquage visuel du mot saisi
                    return mot

                print("Erreur : entrez un mot contenant uniquement des lettres.")
        else:
            print("Erreur : choisissez 1 ou 2.")

"""
BONUS 1
"""

def jouer(scores, fichier):
    """
    Permet de rejouer au Pendu après chaque partie et de comptabiliser les victoires.

    Paramètres :
        scores (dict) : Dictionnaire des scores des joueurs.
        fichier (str ou Path) : Chemin du fichier de sauvegarde.

    Retour :
        None
    """
    while True:  # Boucle de rejouabilité
        nom = input("Nom du joueur : ").strip()  # Saisie du nom

        if not nom or ":" in nom:
            print("Erreur : nom invalide.")
            continue

        scores.setdefault(nom, 0.0)  # Ajoute le joueur avec 0 victoire s'il n'existe pas

        mot = choisir_mode()  # Choix du mode
        resultat = jouer_pendu(mot) if mot else "Erreur : aucun mot disponible."

        print(resultat)

        if resultat.startswith("Gagné"):  # Vérification de la victoire
            scores[nom] += 1  # Ajout d'une victoire

        print(f"{nom} : {scores[nom]} victoire(s)")  # Affichage du score
        sauvegarder_scores(scores, fichier)  # Sauvegarde après chaque partie

        while True:
            reponse = input("\nRejouer ? (o/n) : ").strip().lower()

            if reponse in ("o", "n"): break
            print("Erreur : entrez o ou n.")

        if reponse == "n":
            print("Merci d'avoir joué !")
            break

def charger_scores(fichier):
    """
    Charge les scores des joueurs depuis un fichier texte.

    Paramètre :
        fichier (str) : Fichier contenant les scores.

    Retour :
        dict : Dictionnaire des joueurs et de leurs victoires.
    """
    scores = {}

    try:
        with open(fichier, "r", encoding="utf-8") as f:  # Ouverture en lecture
            for ligne in f:  # Lecture ligne par ligne
                ligne = ligne.strip()  # Suppression des espaces inutiles

                if not ligne: continue  # Ignore les lignes vides

                if ligne.count(":") != 1:  # Vérification du format
                    print(f"Ligne mal formée : {ligne}")
                    continue

                nom, victoires = ligne.split(":")  # Séparation des données
                nom = nom.strip()

                if not nom:  # Vérification du nom
                    print("Erreur : nom vide.")
                    continue

                try:
                    victoires = float(victoires)  # Conversion en float
                except ValueError:
                    print(f"Score invalide pour {nom}.")
                    continue

                if not math.isfinite(victoires) or victoires < 0:
                    print(f"Score invalide pour {nom}.")
                    continue

                scores[nom] = victoires  # Ajout du joueur et de son score

    except FileNotFoundError:
        pass  # Premier lancement : aucun score enregistré

    except (OSError, UnicodeError) as e:
        print(f"Erreur de lecture : {e}")

    return scores

def sauvegarder_scores(scores, fichier):
    """
    Sauvegarde les scores des joueurs dans un fichier texte
    au format nom:victoires.

    Paramètres :
        scores (dict) : Dictionnaire des joueurs et de leurs victoires.
        fichier (str) : Nom du fichier de sauvegarde.

    Retour :
        None
    """
    try:
        with open(fichier, "w", encoding="utf-8") as f:  # Ouverture en écriture
            for nom, victoires in scores.items():  # Parcours des scores
                f.write(f"{nom}:{float(victoires)}\n")  # Sauvegarde du score

    except OSError as e:  # Gestion des erreurs d'écriture
        print(f"Erreur de sauvegarde : {e}")

if __name__ == "__main__":
    fichier = Path(__file__).with_name("scores.txt")  # Chemin du fichier des scores
    scores = charger_scores(fichier)  # Chargement des scores
    jouer(scores, fichier)  # Lancement et sauvegarde après chaque partie
