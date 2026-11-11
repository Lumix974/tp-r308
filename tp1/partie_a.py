from pathlib import Path

dic = {}  # Dictionnaire des étudiants

def ajouter_etudiant(d, nom, note):
    """
    Ajoute un étudiant au dictionnaire ou modifie sa note s'il existe déjà.
    La note doit être comprise entre 0 et 20.

    Paramètres :
        d (dict) : Dictionnaire contenant les étudiants et leurs notes.
        nom (str) : Nom de l'étudiant.
        note (float) : Note de l'étudiant.

    Retour :
        dict : Dictionnaire mis à jour.
    """
    try:
        note = float(note)  # Conversion en float

        if 0 <= note <= 20:  # Vérification de la note
            d[nom] = note  # Ajout ou modification de l'étudiant
        else:
            print("Erreur : la note doit être entre 0 et 20.")

    except (ValueError, TypeError):  # Erreur de conversion
        print("Erreur : la note doit être un nombre.")

    return d

def moyenne_classe(d):
    """
    Calcule la moyenne des notes des étudiants.
    La moyenne est arrondie à deux décimales.

    Paramètres :
        d (dict) : Dictionnaire contenant les étudiants et leurs notes.

    Retour :
        float : Moyenne des notes.
        None : Si le dictionnaire est vide.
    """
    return round(sum(d.values()) / len(d), 2) if d else None # Calcul de la moyenne avec vérification du dictionnaire vide, arrondi à 2 décimales

def meilleur_etudiant(d):
    """
    Recherche l'étudiant ayant la meilleure note dans le dictionnaire.

    Paramètres :
        d (dict) : Dictionnaire contenant les étudiants et leurs notes.

    Retour :
        tuple : Nom et note du meilleur étudiant.
        None : Si le dictionnaire est vide.
    """
    if not d: return None  # Vérification du dictionnaire vide

    meilleur_nom = ""
    meilleure_note = -1

    for nom, note in d.items():  # Parcours des étudiants
        if note > meilleure_note:  # Comparaison des notes
            meilleure_note, meilleur_nom = note, nom

    return (meilleur_nom, meilleure_note)  # Retourne un tuple

def sauvegarder_etudiants(d, fichier):
    """
    Sauvegarde les étudiants et leurs notes dans un fichier texte.
    Chaque ligne du fichier respecte le format nom:note.

    Paramètres :
        d (dict) : Dictionnaire contenant les étudiants et leurs notes.
        fichier (str) : Nom ou chemin du fichier de sauvegarde.

    Retour :
        None : La fonction ne retourne aucune valeur.
    """
    try:
        with open(fichier, "w", encoding="utf-8") as f:  # Ouverture en écriture
            for nom, note in d.items():  # Parcours du dictionnaire
                f.write(f"{nom}:{note}\n")  # Écriture dans le fichier

    except OSError as e:  # Gestion des erreurs d'écriture
        print(f"Erreur de sauvegarde : {e}")

def charger_etudiants(fichier):
    """
    Charge les étudiants et leurs notes depuis un fichier texte.
    Ignore les lignes vides ou mal formées et gère les erreurs de lecture.

    Paramètres :
        fichier (str) : Nom ou chemin du fichier à charger.

    Retour :
        dict : Dictionnaire contenant les étudiants chargés.
               Retourne un dictionnaire vide si le fichier est absent.
    """
    d = {}  # Dictionnaire pour les données chargées

    try:
        with open(fichier, "r", encoding="utf-8") as f:  # Ouverture en lecture
            for ligne in f:  # Lecture ligne par ligne
                ligne = ligne.strip()  # Suppression des espaces inutiles

                if not ligne: continue  # Ignore les lignes vides

                if ligne.count(":") != 1:  # Vérification du format
                    print(f"Ligne mal formée : {ligne}")
                    continue

                nom, note = ligne.split(":")  # Séparation nom et note
                nom = nom.strip()
                note = note.strip()

                if not nom:  # Vérification du nom
                    print("Erreur : nom vide.")
                    continue

                ajouter_etudiant(d, nom, note)  # Ajout de l'étudiant

    except FileNotFoundError:  # Fichier inexistant
        print("Erreur : fichier introuvable.")

    except OSError as e:  # Autres erreurs de lecture
        print(f"Erreur de lecture : {e}")

    return d

# Tests du programme
if __name__ == "__main__":
    ajouter_etudiant(dic, "Alice", 12)
    ajouter_etudiant(dic, "Bob", 15)
    ajouter_etudiant(dic, "Claire", 9.5)

    print("Étudiants :", dic)
    print("Moyenne :", moyenne_classe(dic))
    print("Meilleur étudiant :", meilleur_etudiant(dic))

    fichier = Path(__file__).with_name("etudiants.txt")  # Chemin du fichier
    sauvegarder_etudiants(dic, fichier)  # Sauvegarde des étudiants
    dic_charge = charger_etudiants(fichier)  # Chargement des étudiants

    print("Dictionnaire rechargé :", dic_charge)