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
# jeu.py
# Classe du jeu
#
# Cette classe contient les données du jeu
# Elle inclus les objets de type personnage
# On peut:
# - L'initialiser avec un nouveau jeu vide (création par défaut)
# - Lui ajouter des personnages
# - Lui retirer des personnages
# - Sélectionner un personnage
# - Mettre à jour les données du personnage
# - La charger depuis un fichier texte
# - La sauvegarder dans un fichier texte
#
# On stocke les données dans des fichiers de type texte au format JSON (Javascript Object Notation)
# Les fichiers sont sous le même répertoire que l'application
# Afin de discriminer les fichier invalides on ajoute un entête unique à chaque fichier
#
# La gestion des fichiers est volontairement simplifiée et pourra être améliorée
# - On ne demande pas de confirmation si on ecrase un fichier existant
# - On considère les données du fichier valide à partir du moment ou l'entête correct est présent
# - On ne contrôle pas que les données ont été correctement sauvées avant de fermer ou ouvrir un autre fichier
#
# La création depuis le corps de programme main est:
#  from jeu import Jeu
#  job = Jeu()
# Les appels depuis la classe fenêtre sont:
#  job.nouveau()
#  liste = job.ouvrir()
#  job.enregistrer()
#  job.enregistrer_sous()
#  data = job.fermer()
#  personnage = job.creer()
#  personnage = job.selectionner(index)
#  string = job.valider(personnage)
#  dictionnaire = job.lancer(integer, integer)
#

import os
import json
import random
from tkinter import filedialog, messagebox
import personnage

class Jeu:
    def __init__(self):

        # Entête magique des fichiers jeux
        self.magic = "MAGIC-ISN-V3.0"

        # par défaut les fichiers sont stockés dans le répertoire du jeu
        self.rep = os.getcwd()

        # A l'initialisation aucun fichier jeu n'est chargé et les données sont vierges
        # Il n'y a pas de personnages
        self.filename = ''
        self.data = []
        self.current = None

    # Nouveau jeu de données
    # On efface la liste des personnages
    def nouveau(self):

        self.data = []
        self.current = None
        return

    # Commande d'ouverture d'un fichier jeu
    # On va utiliser une boite de dialogue système pour choisir un fichier
    def ouvrir(self):

        # Choix d'un fichier dans le répertoire courant
        # Les fichiers sont de type texte (.txt) ou tous types (.*)
        filename = filedialog.askopenfilename(
            title="Ouvrir",
            initialdir=self.rep,
            filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))

        # Le dialogue renvoie une chaine vide si abandon de l'utilisateur
        if len(filename) > 0:

            # On conserve le nom du fichier utilisé
            self.filename = filename

            # Lecture du fichier
            try:
                fp = open(self.filename, "r")
            except:
                messagebox.showwarning(
                    "Ouvrir",
                    "Impossible d'ouvrir le fichier\n(%s)" % self.filename
                )
                return None

            # Vérification de l'entête magique (avec version du fichier)
            magic_string = fp.read(len(self.magic))
            if magic_string != self.magic:
                fp.close()
                messagebox.showwarning(
                    "Ouvrir",
                    "Le fichier n'est pas au bon format"
                )
                return None

            # Lecture du Dictionnaire au format JSON
            json_string = fp.read()
            fp.close()

            # Conversion du format JSON en liste
            self.data = json.loads(json_string)

            # Extrait la liste des noms de personnages
            # La liste names sera envoyée à Fenêtre pour affichage
            # En premier on met le nom du fichier
            # Ensuite les noms de personnages
            names = []
            names.append(filename)
            for person in self.data:
                names.append(person["Fiche"]["Nom"])
            return names

        # Pas de fichier ouvert on renvoie None
        # Qui sera traité comme un abandon de la commande par Fenêtre
        else:
            return None

    # commande enregistrer sous le nom par défaut
    def enregistrer(self):

        # L'enregistrement n'est possible que si un fichier existe
        if len(self.filename) > 0:

            # Conversion du Dictionnaire en JSON
            json_string = json.dumps(self.data)

            # Ecriture dans le fichier
            # On ecrase tout fichier existant
            fp = open(self.filename, "w")

            # Ecriture de l'entête magique
            fp.write(self.magic)

            # Ecriture du Dictionnaire
            fp.write(json_string)
            fp.close()

        else:
            messagebox.showwarning(
                "Enregistrer",
                "Aucun fichier sélectionné pour enregistrer"
            )
        return

    # commande enregistrer sous un nouveau nom
    def enregistrer_sous(self):

        # Choix d'un fichier dans le répertoire courant
        filename = filedialog.asksaveasfilename(
            title="Enregistrer sous",
            initialdir=self.rep,
            initialfile=self.filename,
            filetypes=(("Text File", "*.txt"), ("All Files", "*.*"))
        )
        if len(filename) > 0:
            # On conserve le nom du fichier utilisé
            name, extension = os.path.splitext(filename)
            if extension == '':
                extension = 'txt'
            self.filename = name + '.' + extension
            self.enregistrer()
        return

    # commande fermer le fichier jeu
    def fermer(self):

        self.filename = None
        self.data = []
        return None

    # commande de création d'un personnage
    # il faut un jeu actif
    def creer(self):

        # On ajoute un personnage à la liste de données du jeu (data)
        # la position courante est mémorisée (fin de la liste)
        # on renvoie le personnage à la fenêtre
        pod = personnage.creer()
        self.data.append(pod)
        self.current = len(self.data)-1
        return pod

    # selection d'un personnage dans la liste
    def selectionner(self, index):

        # ne peut être que de 0 à nombre-1 de la liste
        if index < len(self.data):
            self.current = index
            return self.data[index]
        else:
            return None

    # Changement de partie
    # On doit modifier les compétences de tous les personnages sans toucher aux caractéristiques
    # Renvoie le personnage courant
    def partie(self):
        # Nécessite de crééer la feuille d'archétype.
        # Fait appel à la feuille d'archétype pour archiver les compétences du personnage
        return self.data[self.current]

    # demande de validation et enregistrement des données du personnage
    # On vérifie la validité des données
    # Si les données sont correctes:
    # - le personnage est stocké dans la liste
    # - l'index, le nom et un message de succès sont renvoyés à l'interface
    # Sinon le message d'erreur fourni par la vérification du personnage est renvoyé
    def valider(self, pod):

        message = personnage.verifier(pod)
        if message is not None:
            return {"index": None, "nom": None, "message": message}

        # On recalcule tous les champs
        pod = personnage.recalculer(pod)

        self.data[self.current] = pod
        Nom = pod["Fiche"]["Nom"]
        return {"index":self.current, "nom":Nom, "message":''}

    # Lancer des dés
    # On commence par calculer le seuil de réussite à partir des points en caractéristiques et compétences
    # On détermine ensuite les seuils de jugement de réussite ou échec (significatif, particulier, total)
    # On lance les dés et on compare les résultats aux seuils
    # On renvoie à l'interface les résultats
    def lancer(self, caracteristique, competence):

        # Seuil obtenu à partir du tableau de résolution
        seuil = self.calcul(caracteristique, competence)

        # Calcul des seuils de jugement
        # - c'est une "réussite particulière" si le tirage est inférieur à 20% du seuil
        # - c'est une "réussite significative" si le tirage est inférieur à 50% du seuil
        # - c'est une "réussite" si le tirage est inférieur ou égal au seuil
        # - on ne peut pas échouer si le seuil est supérieur à 100
        # - c'est un "échec total" si le tirage est supérieur à 90% de 100-seuil
        # - c'est un "échec particulier" si le tirage est supérieur à 80% de 100-seuil
        # - c'est un "échec" si le tirage est supérieur au seuil
        reussi_particulier = 0.2 * seuil
        reussi_significatif = 0.5 * seuil
        if seuil > 100:
            echec_total = 180
            echec_particulier = 180
        else:
            echec_total = seuil + 0.9 * (100 - seuil)
            echec_particulier = seuil + 0.8 * (100 - seuil)

        # lancer des dés
        des = self.des()

        # jugement
        if des <= reussi_particulier:
            special = "réussite particulière"
        elif des <= reussi_significatif:
            special = "réussite significative"
        elif des <= seuil:
            special = "réussite"
        elif seuil < 100:
            if des > echec_total:
                special = "échec total"
            elif des > echec_particulier:
                special = "échec particulier"
            else:
                special = "échec"
        else:
            special = "réussite"

        # renvoi du résultat du tirage à l'interface graphique pour affichage
        # on retourne un dictionnaire : seuil, tirage et special
        tirage = {"seuil": seuil, "tirage": des, "special": special}
        return tirage

    # Fonction de calcul du Seuil de points de 0 à 170
    # Ce seuil sera utilisé pour déterminer le succès ou non de l'action en cours pour le personnage
    def calcul(self,caracteristique,competence):

        # On utilise la formule plutôt que le tableau du livre
        return int(caracteristique * (1 + .5 * (competence + 8)))

    # Lancer de dés
    # On lance 2 dés à 10 faces donnant un résultat entre 1 et 100
    def des(self):

        # On lance bien 2 dés
        unit = random.randrange(0, 9)
        dix = random.randrange(0, 9)
        score = 10 * dix + unit

        # Le résultat 0-0 est interprèté comme 100
        if score == 0:
            score = 100
        return score
