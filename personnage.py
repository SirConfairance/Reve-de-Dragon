# Rêve de Dragon
# ISN Terminale S Lycée Murat Issoire 2016-2017
# Par Jikael Larriven, Marguerite Sobkowicz, Cédric Mongiat
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# personnage.py
# Dictionnaire des personnages
#
# Comporte les définitions du dictionnaire contenant chaque personnage
# Applique les règles du jeu relatives aux personnages
# Les fonctions permettent les traitements sur le dictionnaire :
# - creer : création d'un personnage vide
# - caracteristiques, competence, point : renvoient les textes correspondant aux index
# - verifier : vérification de la cohérence des données du personnage par rapport aux règles d'attribution des points
# - calculer : calcul des caractéristiques du personnage à partir des valeurs saisies ou modifiées
#

from math import *

# La fonction creer retourne un dictionnaire de personnage avec des données de base
def creer():

    person = {
        "Version": 0,
        "Fiche": {
            "Nom": "",
            "Heure_Naissance": "",
            "Sexe": "M",
            "Age": 0,
            "Taille": 0,
            "Poids": 0,
            "Cheveux": "",
            "Yeux": "",
            "Beaute": 0,
            "Signes_Particulier": "",
            "Ambidextre": 0,
            "Haut_Revant": 0
        },
        "Point": {
            "Vie": 0,
            "Endurance": 0,
            "Seuil_Constitution": 0,
            "Sustain": 0,
            "PlusDmg": 0,
            "Malus_Armor": 0,
            "Encombrement": 0
        },
        "Caracteristique": {
            "Taille": 0,
            "Apparence": 0,
            "Constitution": 0,
            "Force": 0,
            "Agilite": 0,
            "Dexterite": 0,
            "Vue": 0,
            "Ouie": 0,
            "Odorat_Gout": 0,
            "Volonte": 0,
            "Intellect": 0,
            "Empathie": 0,
            "Reve": 0,
            "Chance": 0,
            "Tir": 0,
            "Melee": 0,
            "Lancer": 0,
            "Derobee": 0
        },
        "Competence": {
            "Generale": {
                "Bricolage": -4,
                "Chant": -4,
                "Course": -4,
                "Cuisine": -4,
                "Dance": -4,
                "Dessin": -4,
                "Discretion": -4,
                "Escalade": -4,
                "Saut": -4,
                "Seduction": -4,
                "Vigilance": -4
            },
            "Particuliere": {
                "Charpenterie": -8,
                "Comedie": -8,
                "Commerce": -8,
                "Equitation": -8,
                "Maconnerie": -8,
                "Musique": -8,
                "Pick_Pocket": -8,
                "Survie_Cite": -8,
                "Survie_Exterieur": -8,
                "Desert": -8,
                "Foret": -8,
                "Glaces": -8,
                "Marais": -8,
                "Montagnes": -8
            },
            "Specialisee": {
                "Acrobatie": -11,
                "Chirurgie": -11,
                "Jeu": -11,
                "Jonglerie": -11,
                "Maroquinerie": -11,
                "Metallurgie": -11,
                "Natation": -11,
                "Navigation": -11,
                "Orfevrerie": -11,
                "Serrurerie": -11
            },
            "Connaissances": {
                "Alchimie": -11,
                "Astronomie": -11,
                "Botanique": -11,
                "Ecriture": -11,
                "Legendes": -11,
                "Medecine": -11,
                "Zoologie": -11
            },
            "Draconic": {
                "Oniros": -11,
                "Hypnos": -11,
                "Narcos": -11,
                "Thanatos": -11
            }
        }
    }
    return person

# Détermine la cléet le texte d'affichage associés à un index de caractéristiques
def caracteristique(num1,num2):
    case = {
        (0, 0): "Taille",
        (0, 1): " Taille",
        (1, 0): "Apparence",
        (1, 1): " Apparence",
        (2, 0): "Constitution",
        (2, 1): " Constitution",
        (3, 0): "Force",
        (3, 1): " Force",
        (4, 0): "Agilite",
        (4, 1): " Agilité",
        (5, 0): "Dexterite",
        (5, 1): " Dexterité",
        (6, 0): "Vue",
        (6, 1): " Vue",
        (7, 0): "Ouie",
        (7, 1): " Ouie",
        (8, 0): "Odorat_Gout",
        (8, 1): " Odorat-Gout",
        (9, 0): "Volonte",
        (9, 1): " Volonté",
        (10, 0): "Intellect",
        (10, 1): " Intellect",
        (11, 0): "Empathie",
        (11, 1): " Empathie",
        (12, 0): "Reve",
        (12, 1): " Rêve",
        (13, 0): "Chance",
        (13, 1): " Chance",
        (14, 0): "Tir",
        (14, 1): " Tir",
        (15, 0): "Melee",
        (15, 1): " Melée",
        (16, 0): "Lancer",
        (16, 1): " Lancer",
        (17, 0): "Derobee",
        (17, 1): " Derobée"
    }
    return case.get((num1,num2))

# Détermine les clés et le texte associées à un index de compétence
def competence(num1,num2):
    case = {
        (0, 0): "Generale",
        (0, 1): "Bricolage",
        (0, 2): " Bricolage",
        (1, 0): "Generale",
        (1, 1): "Chant",
        (1, 2): " Chant",
        (2, 0): "Generale",
        (2, 1): "Course",
        (2, 2): " Course",
        (3, 0): "Generale",
        (3, 1): "Cuisine",
        (3, 2): " Cuisine",
        (4, 0): "Generale",
        (4, 1): "Dance",
        (4, 2): " Dance",
        (5, 0): "Generale",
        (5, 1): "Dessin",
        (5, 2): " Dessin",
        (6, 0): "Generale",
        (6, 1): "Discretion",
        (6, 2): " Discretion",
        (7, 0): "Generale",
        (7, 1): "Escalade",
        (7, 2): " Escalade",
        (8, 0): "Generale",
        (8, 1): "Saut",
        (8, 2): " Saut",
        (9, 0): "Generale",
        (9, 1): "Seduction",
        (9, 2): " Séduction",
        (10, 0): "Generale",
        (10, 1): "Vigilance",
        (10, 2): " Vigilance",
        (11, 0): "Particuliere",
        (11, 1): "Charpenterie",
        (11, 2): " Charpenterie",
        (12, 0): "Particuliere",
        (12, 1): "Comedie",
        (12, 2): " Comédie",
        (13, 0): "Particuliere",
        (13, 1): "Commerce",
        (13, 2): " Commerce",
        (14, 0): "Particuliere",
        (14, 1): "Equitation",
        (14, 2): " Equitation",
        (15, 0): "Particuliere",
        (15, 1): "Maconnerie",
        (15, 2): " Maçonnerie",
        (16, 0): "Particuliere",
        (16, 1): "Musique",
        (16, 2): " Musique",
        (17, 0): "Particuliere",
        (17, 1): "Pick_Pocket",
        (17, 2): " Pick Pocket",
        (18, 0): "Particuliere",
        (18, 1): "Survie_Cite",
        (18, 2): " Survie Cité",
        (19, 0): "Particuliere",
        (19, 1): "Survie_Exterieur",
        (19, 2): " Survie Extérieur",
        (20, 0): "Particuliere",
        (20, 1): "Desert",
        (20, 2): " Désert",
        (21, 0): "Particuliere",
        (21, 1): "Foret",
        (21, 2): " Forêt",
        (22, 0): "Particuliere",
        (22, 1): "Glaces",
        (22, 2): " Glaces",
        (23, 0): "Particuliere",
        (23, 1): "Marais",
        (23, 2): " Marais",
        (24, 0): "Particuliere",
        (24, 1): "Montagnes",
        (24, 2): " Montagnes",
        (25, 0): "Specialisee",
        (25, 1): "Acrobatie",
        (25, 2): " Acrobatie",
        (26, 0): "Specialisee",
        (26, 1): "Chirurgie",
        (26, 2): " Chirurgie",
        (27, 0): "Specialisee",
        (27, 1): "Jeu",
        (27, 2): " Jeu",
        (28, 0): "Specialisee",
        (28, 1): "Jonglerie",
        (28, 2): " Jonglerie",
        (29, 0): "Specialisee",
        (29, 1): "Maroquinerie",
        (29, 2): " Maroquinerie",
        (30, 0): "Specialisee",
        (30, 1): "Metallurgie",
        (30, 2): " Métallurgie",
        (31, 0): "Specialisee",
        (31, 1): "Natation",
        (31, 2): " Natation",
        (32, 0): "Specialisee",
        (32, 1): "Navigation",
        (32, 2): " Navigation",
        (33, 0): "Specialisee",
        (33, 1): "Orfevrerie",
        (33, 2): " Orfèvrerie",
        (34, 0): "Specialisee",
        (34, 1): "Serrurerie",
        (34, 2): " Serrurerie",
        (35, 0): "Connaissances",
        (35, 1): "Alchimie",
        (35, 2): " Alchimie",
        (36, 0): "Connaissances",
        (36, 1): "Astronomie",
        (36, 2): " Astronomie",
        (37, 0): "Connaissances",
        (37, 1): "Botanique",
        (37, 2): " Botanique",
        (38, 0): "Connaissances",
        (38, 1): "Ecriture",
        (38, 2): " Ecriture",
        (39, 0): "Connaissances",
        (39, 1): "Legendes",
        (39, 2): " Légendes",
        (40, 0): "Connaissances",
        (40, 1): "Medecine",
        (40, 2): " Médecine",
        (41, 0): "Connaissances",
        (41, 1): "Zoologie",
        (41, 2): " Zoologie",
        (42, 0): "Draconic",
        (42, 1): "Oniros",
        (42, 2): " Oniros",
        (43, 0): "Draconic",
        (43, 1): "Hypnos",
        (43, 2): " Hypnos",
        (44, 0): "Draconic",
        (44, 1): "Narcos",
        (44, 2): " Narcos",
        (45, 0): "Draconic",
        (45, 1): "Thanatos",
        (45, 2): " Thanatos"
    }
    return case.get((num1, num2))

# Détermine la clé et le texte d'affichage associés à un index de points
def point(num1,num2):
    case = {
        (0, 0): "Vie",
        (0, 1): "Vie",
        (1, 0): "Endurance",
        (1, 1): "Endurance",
        (2, 0): "Encombrement",
        (2, 1): "Encombrement",
        (3, 0): "PlusDmg",
        (3, 1): "Bonus aux Dommages",
        (4, 0): "Malus_Armor",
        (4, 1): "  Malus Armure",
        (5, 0): "Seuil_Constitution",
        (5, 1): "  Seuil de Constitution",
        (6, 0): "Sustain",
        (6, 1): "  Seuil de Sustentation"
    }
    return case.get((num1, num2))

# La fonction verifier assure que les données du personnage sont valides
# Elle est utilisée après les saisies
# Elle retourne un message d'erreur texte ou None
def verifier (person):

    # Vérification de l'identification
    if len(person["Fiche"]["Nom"]) < 3:
        return "Le Nom du personnage\ndoit être au moins de 3 caractères"

    # Taille  de 6 à 15
    # Beauté 1 à 16, les points au dessus de 10 sont retranchés des caractéristiques
    # Poids de 31 à 110, à vérifier selon la taille
    # Heure de naissance de 1 à 12


    # Vérification des valeurs limites de caractéristiques à la création du personnage
    # On utilise Version qui vaut 0 à la création et s'incrémente à chaque recalcul des points
    # On ne compte l'affectation des 160 points que lors de la première saisie
    cpt = 0
    for i in range(0, 14):
        ca = person["Caracteristique"][caracteristique(i, 0)]
        if ca < 0:
            return "La valeur minimale pour la caractéristique\n" + caracteristique(i, 1) + " est de 0"
        if ca > 20:
            return "La valeur maximale pour la caractéristique\n" + caracteristique(i, 1) + " est de 20"
        cpt += ca
    if person["Version"] < 1:
        if cpt < 160:
            return "Vous n'avez affecté que " + str(cpt) + " points aux caractéristiques\n Vous disposez de 160 points"
        if cpt > 160:
            return "Vous avez affecté " + str(cpt) + " points aux caractéristiques\n Vous ne disposez que de 160 points"

    # Vérification du nombre de points de compétences à distribuer
    # (selon le livre de règles page 22)
    x = 3000
    # si draconic -350

    # Competences générales
    for i in range(0, 11):

        # Les compétences générales ne peuvent pas être inférieures à -4
        cg = person["Competence"]["Generale"][competence(i, 1)]
        if cg < -4:
            return "La valeur minimale pour la compétence\n" + competence(i, 2) + " est de -4"

        # Decalage de 4 pour avoir des indices partant de 0
        v = 4 + cg
        g = -4

        # On compte les points utilisés par tranches de niveaux
        for j in range(v):
            g += 1
            # de -3 à 0 : 15 points
            if g <= 0:
                x -= 15
            # de +1 à +20 : 20 points
            if g >= 1:
                x -= 20

    # Competences particulières
    for i in range(11, 25):

        # Les compétences particulières ne peuvent pas être inférieures à -8
        cp = person["Competence"]["Particuliere"][competence(i, 1)]
        if cp < -8:
            return "La valeur minimale pour la compétence\n" + competence(i, 2) + " est de -8"

        # Decalage de 8 pour avoir des indices partant de 0
        v = 8 + cp
        p = -8

        # On compte les points utilisés par tranches de niveaux
        for j in range(v):
            p += 1
            # de -7 à -4 : 10 points
            if p <= -4:
                x -= 10
            # de -3 à 0 : 15 points
            if p >= -3 and p <= 0:
                x -= 15
            # de +1 à +20 : 20 points
            if p >= 1:
                x -= 20

    # Competences spécialisées
    for i in range(25, 35):

        # Les compétences spécialisées ne peuvent pas être inférieures à -11
        cs = person["Competence"]["Specialisee"][competence(i, 1)]
        if cs < -11:
            return "La valeur minimale pour la compétence\n" + competence(i, 2) + " est de -11"

        # Decalage de 11 pour avoir des indices partant de 0
        v = 11 + cs
        scd = -11

        # On compte les points utilisés par tranches de niveaux
        for j in range(v):
            scd += 1
            # de -11 à -8 : 5 points
            if scd >= -11 and scd <= -8:
                x -= 5
            # de -7 à -4 : 10 points
            if scd >= -7 and scd <= -4:
                x -= 10
            # de -3 à 0 : 15 points
            if scd >= -3 and scd <= 0:
                x -= 15
            # de +1 à +20 : 20 points
            if scd >= 1:
                x -= 20

    # Competences connaissances
    for i in range(35, 42):

        # Les compétences connaissances ne peuvent pas être inférieures à -11
        cc = person["Competence"]["Connaissances"][competence(i, 1)]
        if cc < -11:
            return "La valeur minimale pour la compétence\n" + competence(i, 2) + " est de -11"

        # Decalage de 11 pour avoir des indices partant de 0
        v = 11 + cc
        scd = -11

        # On compte les points utilisés par tranches de niveaux
        for j in range(v):
            scd += 1
            # de -11 à -8 : 5 points
            if scd >= -11 and scd <= -8:
                x -= 5
            # de -7 à -4 : 10 points
            if scd >= -7 and scd <= -4:
                x -= 10
            # de -3 à 0 : 15 points
            if scd >= -3 and scd <= 0:
                x -= 15
            # de +1 à +20 : 20 points
            if scd >= 1:
                x -= 20

    # Competences draconic sauf Thanatos
    for i in range(42, 45):

        # Les compétences draconic ne peuvent pas être inférieures à -11
        cd = person["Competence"]["Draconic"][competence(i, 1)]
        if cd < -11:
            return "La valeur minimale pour la compétence\n" + competence(i, 2) + " est de -11"

        # Decalage de 11 pour avoir des indices partant de 0
        v = 11 + cd
        scd = -11

        # On compte les points utilisés par tranches de niveaux
        for j in range(v):
            scd += 1
            # de -11 à -8 : 5 points
            if scd >= -11 and scd <= -8:
                x -= 5
            # de -7 à -4 : 10 points
            if scd >= -7 and scd <= -4:
                x -= 10
            # de -3 à 0 : 15 points
            if scd >= -3 and scd <= 0:
                x -= 15
            # de +1 à +20 : 20 points
            if scd >= 1:
                x -= 20

    # Competences draconic Thanatos
    # Les compétences draconic ne peuvent pas être inférieures à -11
    ct = person["Competence"]["Draconic"]["Thanatos"]
    if ct < -11:
        return "La valeur minimale pour la compétence Thanatos\n est de -11"

    # Decalage de 11 pour avoir des indices partant de 0
    v = 11 + ct
    scd = -11

    # On compte les points utilisés par tranches de niveaux
    for j in range(v):
        scd += 1
        # de -11 à -8 : 10 points
        if scd >= -11 and scd <= -8:
            x -= 10
        # de -7 à -4 : 20 points
        if scd >= -7 and scd <= -4:
            x -= 20
        # de -3 à 0 : 30 points
        if scd >= -3 and scd <= 0:
            x -= 30
        # de +1 à +20 : 40 points
        if scd >= 1:
            x -= 40

    if x > 0:
        return "Il reste encore " + str(x) + " points"

    elif x < 0:
        return "Attention le seuil de point est dépassé de " + str(-x) + " points"

    return None

# La fonction calculer met à jour le personnage à partir des données saisie
# Elle recalcule les valeur qui dépendent d'autres valeurs
# Elle retourne le dictionnaire personnage modifié
def recalculer (person):

    TabConst = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
    TabTaille = [0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5]

    # calcul des caractéristiques (selon le livre de règles page 11)
    person["Caracteristique"]["Melee"] = (person["Caracteristique"]["Force"] + person["Caracteristique"]["Agilite"]) // 2
    person["Caracteristique"]["Tir"] = (person["Caracteristique"]["Vue"] + person["Caracteristique"]["Dexterite"]) // 2
    person["Caracteristique"]["Lancer"] = (person["Caracteristique"]["Tir"] + person["Caracteristique"]["Force"]) // 2
    person["Caracteristique"]["Derobee"] = (person["Caracteristique"]["Agilite"] + 21 - person["Caracteristique"]["Taille"]) // 2

    # calcul des points (formules du livre page 22)
    person["Point"]["Vie"] = (person["Caracteristique"]["Taille"] + person["Caracteristique"]["Constitution"]) / 2
    person["Point"]["Endurance"] = person["Caracteristique"]["Taille"] + person["Caracteristique"]["Constitution"]
    person["Point"]["Seuil_Constitution"] = TabConst[person["Caracteristique"]["Constitution"]]
    person["Point"]["Sustain"] = TabTaille[person["Caracteristique"]["Taille"]]
    person["Point"]["PlusDmg"] = floor((person["Caracteristique"]["Taille"] + person["Caracteristique"]["Force"]) / 2)
    person["Point"]["Encombrement"] = (person["Caracteristique"]["Taille"] + person["Caracteristique"]["Force"]) / 2

    # Incrément de la version du personnage
    person["Version"] += 1

    return person
