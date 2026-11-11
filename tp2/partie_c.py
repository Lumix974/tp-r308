
from partie_a import Grille
from partie_b import JoueurHumain, JoueurIA


def jouer_partie(joueurs, affichage=True):
    """
    Lance une partie de Morpion et alterne les joueurs.

    Paramètres :
        joueurs (dict) : Joueurs associés aux symboles X et O.
        affichage (bool) : Active ou désactive l'affichage.

    Retour :
        str : Symbole du gagnant ou None en cas de match nul.
    """
    g = Grille()  # Création de la grille
    symbole = "X"  # Premier joueur

    while True:
        if affichage: g.afficher()  # Affichage de la grille

        coup = joueurs[symbole].prochain_coup(g.grille, symbole)

        if coup is None: return None  # Aucune case disponible

        x, y = coup  # Récupération des coordonnées

        if not g.jouer(x, y, symbole): continue  # Coup invalide

        if g.est_gagnant(symbole):  # Vérification de la victoire
            if affichage:
                g.afficher()
                print(f"\nLe joueur {symbole} a gagné !")
            return symbole

        if g.est_plein():  # Vérification du match nul
            if affichage:
                g.afficher()
                print("\nMatch nul !")
            return None

        symbole = "O" if symbole == "X" else "X"  # Changement de joueur


def choisir_mode():
    """
    Permet de choisir le mode de jeu.

    Retour :
        str : Mode sélectionné.
    """
    while True:
        print("\n1 - Humain contre IA")
        print("2 - Humain contre Humain")
        print("3 - IA contre IA (20 parties)")
        print("0 - Quitter")

        choix = input("Choisissez un mode : ").strip()

        if choix in ("0", "1", "2", "3"): return choix

        print("Erreur : choisissez un mode valide.")


def jouer():
    """
    Lance le Morpion avec plusieurs modes et comptabilise les résultats.

    Retour :
        None
    """
    scores = {"X": 0, "O": 0, "Nuls": 0}  # Initialisation des scores

    while True:
        choix = choisir_mode()  # Sélection du mode

        if choix == "0": break  # Arrêt du programme

        if choix == "1":
            joueurs = {"X": JoueurHumain(), "O": JoueurIA()}
        elif choix == "2":
            joueurs = {"X": JoueurHumain(), "O": JoueurHumain()}
        else:
            joueurs = {"X": JoueurIA(), "O": JoueurIA()}

        nb_parties = 20 if choix == "3" else 1

        for i in range(nb_parties):
            gagnant = jouer_partie(joueurs, choix != "3")

            if gagnant is None:
                scores["Nuls"] += 1  # Comptabilisation d'un match nul
            else:
                scores[gagnant] += 1  # Comptabilisation d'une victoire

            if choix == "3":
                print(f"Partie {i + 1}/20 : {gagnant if gagnant else 'Nul'}")

            print("\n--- Tableau des scores ---")
            print(f"Victoires X : {scores['X']}")
            print(f"Victoires O : {scores['O']}")
            print(f"Matchs nuls : {scores['Nuls']}")
            print(f"Total : {sum(scores.values())} partie(s)")

    print("Merci d'avoir joué !")


if __name__ == "__main__":
    jouer()  # Lancement du Morpion
