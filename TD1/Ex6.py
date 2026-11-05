"""Écrire un dictionnaire représentant un répertoire téléphonique (nom → numéro).
Ajouter 3 entrées, modifier un numéro, supprimer une entrée,
afficher tous les noms et numéros.
"""

# Création d'un dictionnaire vide
dico = {}

# Ajout de 3 personnes avec leur numéro de téléphone
dico["Fabien"] = "0692123456"
dico["Esteban"] = "0692654321"
dico["Manon"] = "0692456789"

# Affichage du dictionnaire après l'ajout des 3 entrées
print(dico)

# Modification du numéro de Fabien
dico["Fabien"] = "0692111111"

# Affichage du dictionnaire après modification
print(dico)

# Suppression de Fabien du dictionnaire
del dico["Fabien"]

# Affichage du dictionnaire après suppression
print(dico)

# Parcours du dictionnaire
# k correspond au nom et v au numéro de téléphone
for k, v in dico.items():
    print(k, v)