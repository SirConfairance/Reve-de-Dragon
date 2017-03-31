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
# fenetre.py
# Classe de gestion de la fenetre
# La classe gère tous les objets affichés dans la fenêtre du programme:
# - Menus, permettant d'activer les commandes
# - Frames, contenant les différents widgets d'affichage
# A sa création, la classe reçoit en paramètre l'objet job de classe Jeu
#
# Utilisation:
#  from fenetre import Fenetre
#  wnd = Fenetre(job)
#
#

from tkinter import Tk, StringVar, IntVar, Label, Entry, BooleanVar, Checkbutton, Listbox, Menu, Frame, LabelFrame, Canvas, \
    PhotoImage, Button, Text, Scrollbar, Toplevel
from tkinter.messagebox import *
import personnage

class Fenetre:

    def __init__(self, root, job):

        # Récupération de l'objet Jeu
        self.jeu = job
        self.saved = True

        # Création de la fenêtre principale
        self.root = root
        self.root.title('Rêve de Dragon')
        self.root.resizable(True, True)

        # Création des menus
        # On a 4 menu principaux : filemenu, cmdmenu, viewmenu et helpmenu
        self.menubar = Menu(root)
        self.root.config(menu=self.menubar)

        # filemenu: menu de manipulation des fichiers contenant les personnages
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Fichier", menu=self.filemenu)
        self.filemenu.add_command(label="Nouveau", command=self.nouveau)
        self.filemenu.add_command(label="Ouvrir", command=self.ouvrir)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Enregistrer", command=self.jeu.enregistrer)
        self.filemenu.add_command(label="Enregistrer sous...", command=self.jeu.enregistrer_sous)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Fermer", command=self.fermer)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Imprimer", command=self.void, state='disabled')
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Quitter", command=self.quitter)

        # cmdmenu: menu des commandes sur les personnages
        self.cmdmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Commande", menu=self.cmdmenu)
        self.cmdmenu.add_command(label="Nouvelle Partie", command=self.partie)
        self.cmdmenu.add_separator()
        self.cmdmenu.add_command(label="Nouveau Personnage", command=self.creer)
        self.cmdmenu.add_separator()
        self.cmdmenu.add_command(label="Valider le Personnage", command=self.valider)

        # viewmenu: menu de sélection du personnage à l'affichage
        # Ce menu est vide en l'absence de personnage
        # Il est rempli au chargement ou à la création d'un personnage
        self.viewmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Personnage", menu=self.viewmenu)

        # helpmenu: menu d'aide
        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Aide", menu=self.helpmenu)
        self.helpmenu.add_command(label="Règles du Jeu", command=self.regles)
        self.helpmenu.add_command(label="Utilisation du Programme", command=self.utilise)
        self.helpmenu.add_command(label="A Propos...", command=self.a_propos)

        # frame1 : Fiche du personnage
        frame1 = Frame(root, borderwidth=0, relief='flat', height=200, width=600)
        frame1.grid(row=0, column=0, sticky='NW', padx="15", pady="5")

        # Nom
        self.Entry_Nom = StringVar()
        self.Old_Nom = ""
        Label(frame1, text='Nom:').grid(row=0, column=0, columnspan=2, sticky='E')
        Entry(frame1, textvariable=self.Entry_Nom, justify='left', width=32)\
            .grid(row=0, column=2, columnspan=4, sticky='W', padx="5")

        # Age
        self.Entry_Age = IntVar()
        Label(frame1, text='Age:').grid(row=1, column=0, columnspan=2, sticky='E')
        Entry(frame1, textvariable=self.Entry_Age, justify='right', width=3)\
            .grid(row=1, column=2, sticky='W', padx="5")

        # Heure de naissance (pour hauts-rêvants)
        self.Entry_Heure = IntVar()
        Label(frame1, text='Heure de Naissance:').grid(row=1, column=3, sticky='E')
        Entry(frame1, textvariable=self.Entry_Heure, justify='right', width=3) \
            .grid(row=1, column=4, sticky='W', padx="5")

        # Taille
        self.Entry_Taille = IntVar()
        Label(frame1, text='Taille:').grid(row=1, column=5, sticky='E')
        Entry(frame1, textvariable=self.Entry_Taille, justify='right', width=3)\
            .grid(row=1, column=6, sticky='W', padx="5")

        # Poids
        self.Entry_Poids = IntVar()
        Label(frame1, text='Poids:').grid(row=1, column=7, sticky='E')
        Entry(frame1, textvariable=self.Entry_Poids, justify='right', width=3)\
            .grid(row=1, column=8, sticky='W', padx="5")

        # Beauté
        self.Entry_Beaute = IntVar()
        Label(frame1, text='Beauté:').grid(row=2, column=0, columnspan=2, sticky='E')
        Entry(frame1, textvariable=self.Entry_Beaute, justify='right', width=3) \
            .grid(row=2, column=2, sticky='W', padx="5")

        # Cheveux
        self.Entry_Cheveux = StringVar()
        Label(frame1, text='Cheveux:').grid(row=2, column=3, sticky='E')
        Entry(frame1, textvariable=self.Entry_Cheveux, justify='left', width=8)\
            .grid(row=2, column=4, sticky='W', padx="5")

        # Yeux
        self.Entry_Yeux = StringVar()
        Label(frame1, text='Yeux:').grid(row=2, column=5, sticky='E')
        Entry(frame1, textvariable=self.Entry_Yeux, justify='left', width=8)\
            .grid(row=2, column=6, sticky='W', padx="5")

        # Haut rêvant
        self.Entry_HRevant = IntVar()
        Checkbutton(frame1, text="Haut-Rêvant", variable=self.Entry_HRevant, command=self.sel_revant) \
            .grid(row=2, column=7, columnspan=2, sticky='W', padx="5")

        # Sexe
        self.Entry_Sexe = StringVar()
        Label(frame1, text='Sexe:').grid(row=3, column=0, columnspan=2, sticky='E')
        Entry(frame1, textvariable=self.Entry_Sexe, justify='left', width=2)\
            .grid(row=3, column=2, sticky='W', padx="5")

        # Ambidextre
        self.Entry_Ambidextre = IntVar()
        Label(frame1, text='Ambidextre:').grid(row=3, column=3, sticky='E')
        Entry(frame1, textvariable=self.Entry_Ambidextre, justify='right', width=3)\
            .grid(row=3, column=4, sticky='W', padx="5")

        # Signes Particuliers
        self.Entry_SignesP = StringVar()
        Label(frame1, text='Signes Particuliers:').grid(row=3, column=5, sticky='E')
        Entry(frame1, textvariable=self.Entry_SignesP, justify='left', width=40)\
            .grid(row=3, column=6, columnspan=3, sticky='W', padx="5")

        # Frame 2 : Caractéristiques
        frame2 = LabelFrame(root, text=" Caractéristiques ", borderwidth=2, relief='ridge', height=200, width=600)
        frame2.grid(row=1, column=0, sticky='NW', padx="10", pady="5")
        frame20 = LabelFrame(frame2, text=' Physiques ', borderwidth=2, relief='ridge', height=200, width=200)
        frame20.grid(row=0, column=0, sticky='NW', padx="5", pady="5")
        frame21 = LabelFrame(frame2, text=' Mentales ', borderwidth=2, relief='ridge', height=200, width=200)
        frame21.grid(row=0, column=1, sticky='NW', padx="5", pady="5")
        frame22 = LabelFrame(frame2, text=' Pouvoirs ', borderwidth=2, relief='ridge', height=200, width=200)
        frame22.grid(row=0, column=2, sticky='NW', padx="5", pady="5")
        frame23 = LabelFrame(frame2, text=' Dérivées ', borderwidth=2, relief='ridge', height=200, width=200)
        frame23.grid(row=0, column=3, sticky='NW', padx="5", pady="5")
        self.Entry_C = []

        # Colonne 0 de taille à Dextérité
        for i in range(0,6):
            self.Entry_C.append(IntVar())
            Label(frame20, text="           "+personnage.caracteristique(i, 1)+':')\
                .grid(row=i, column=0, sticky='E')
            Entry(frame20, textvariable=self.Entry_C[i], justify='right', width=3)\
                .grid(row=i, column=1, sticky='W', padx="5")
        Label(frame20, text=' ').grid(row=6, column=0, sticky='E')

        # Colonne 1 de Vue à Empathie
        for i in range(6, 12):
            self.Entry_C.append(IntVar())
            Label(frame21, text="           "+personnage.caracteristique(i, 1) + ':')\
                .grid(row=i-6, column=0, sticky='E')
            Entry(frame21, textvariable=self.Entry_C[i], justify='right', width=3)\
                .grid(row=i-6, column=1, sticky='W', padx="5")
        Label(frame21, text=' ').grid(row=6, column=0, sticky='E')

        # Colonne 2 de Rêve à Chance
        for i in range(12, 14):
            self.Entry_C.append(IntVar())
            Label(frame22, text="               "+personnage.caracteristique(i, 1) + ':')\
                .grid(row=i-12, column=0, sticky='E')
            Entry(frame22, textvariable=self.Entry_C[i], justify='right', width=3)\
                .grid(row=i-12, column=1, sticky='W', padx="5")
        for i in range(2,7):
            Label(frame22, text=' ').grid(row=i, column=0, sticky='E')

        # Colonne 3 de Tir à Dérobée (ne peuvent être saisies)
        for i in range(14, 18):
            self.Entry_C.append(IntVar())
            Label(frame23, text="             "+personnage.caracteristique(i, 1) + ':')\
                .grid(row=i-14, column=0, sticky='E')
            Entry(frame23, textvariable=self.Entry_C[i], justify='right', width=3, state='disabled')\
                .grid(row=i-14, column=1, sticky='W', padx="5")
        for i in range(4,7):
            Label(frame23, text=' ').grid(row=i, column=0, sticky='E')

        # frame 3 : Points et Seuils (ne peuvent être saisis)
        frame3 = Frame(root, borderwidth=0, relief='flat', height=200, width=600, padx="5", pady="5")
        frame3.grid(row=2, column=0, sticky='NW', padx="10")
        self.Entry_P = []

        # Vie - Endurance - Encombrement
        for i in range(0, 3):
            self.Entry_P.append(IntVar())
            Label(frame3, text=personnage.point(i, 1) + ':').grid(row=0, column=2*i, sticky='E')
            Entry(frame3, textvariable=self.Entry_P[i], justify='right', width=3, state='disabled')\
                .grid(row=0, column=2*i+1, sticky='W', padx="5")

        # Bonus aux Dommages - Malus Armure - Seuil de Constitution - Seuil de Sustentation
        for i in range(3, 7):
            self.Entry_P.append(IntVar())
            Label(frame3, text=personnage.point(i, 1) + ':').grid(row=1, column=2*i-6, sticky='E')
            Entry(frame3, textvariable=self.Entry_P[i], justify='right', width=3, state='disabled')\
                .grid(row=1, column=2*i-5, sticky='W', padx="5")

        # frame 4 : Compétences
        frame4 = LabelFrame(root, text=" Compétences ", borderwidth=2, relief='ridge', height=200, width=600)
        frame4.grid(row=3, column=0, columnspan=2, sticky='NW', padx="10", pady="5")
        frame40 = LabelFrame(frame4, text=' Générales ', borderwidth=2, relief='ridge', height=200, width=200)
        frame40.grid(row=0, column=0, rowspan=2, sticky='NW', padx="5", pady="5")
        frame41 = LabelFrame(frame4, text=' Particulières ', borderwidth=2, relief='ridge', height=200, width=200)
        frame41.grid(row=0, column=1, rowspan=2, sticky='NW', padx="5", pady="5")
        frame42 = LabelFrame(frame4, text=' Spécialisées ', borderwidth=2, relief='ridge', height=200, width=200)
        frame42.grid(row=0, column=2, rowspan=2, sticky='NW', padx="5", pady="5")
        frame43 = LabelFrame(frame4, text=' Connaissances ', borderwidth=2, relief='ridge', height=200, width=200)
        frame43.grid(row=0, column=3, sticky='NW', padx="5", pady="5")
        frame44 = LabelFrame(frame4, text=' Draconic ', borderwidth=2, relief='ridge', height=200, width=200)
        frame44.grid(row=1, column=3, sticky='SW', padx="5", pady="5")
        frame45 = LabelFrame(frame4, text=' Combat Mélée ', borderwidth=2, relief='ridge', height=200, width=200)
        frame45.grid(row=0, column=4, rowspan=2, sticky='NW', padx="5", pady="5")
        frame46 = LabelFrame(frame4, text=' Combat Tir-Lancer ', borderwidth=2, relief='ridge', height=200, width=200)
        frame46.grid(row=0, column=5, rowspan=2, sticky='NW', padx="5", pady="5")
        self.Entry_A = []

        # Colonne 0 : Générales
        for i in range(0, 11):
            self.Entry_A.append(IntVar())
            Label(frame40, text="           "+personnage.competence(i, 2)+':').grid(row=i, column=0, sticky='E')
            Entry(frame40, textvariable=self.Entry_A[i], justify='right', width=3)\
                .grid(row=i, column=1, sticky='W', padx="5")
        for i in range(11, 15):
            Label(frame40, text=' ').grid(row=i, column=0, sticky='E')

        # Colonne 1 : Particulières
        for i in range(11, 25):
            self.Entry_A.append(IntVar())
            Label(frame41, text="      "+personnage.competence(i, 2)+':').grid(row=i-11, column=0, sticky='E')
            Entry(frame41, textvariable=self.Entry_A[i], justify='right', width=3)\
                .grid(row=i-11, column=1, sticky='W', padx="5")
        Label(frame41, text=' ').grid(row=14, column=0, sticky='E')

        # Colonne 2 : Spécialisées
        for i in range(25, 35):
            self.Entry_A.append(IntVar())
            Label(frame42, text="       "+personnage.competence(i, 2)+':')\
                .grid(row=i-25, column=0, sticky='E')
            Entry(frame42, textvariable=self.Entry_A[i], justify='right', width=3)\
                .grid(row=i-25, column=1, sticky='W', padx="5")
        for i in range(10, 15):
            Label(frame42, text=' ').grid(row=i, column=0, sticky='E')

        # Colonne 3: Connaissances
        for i in range(35, 42):
            self.Entry_A.append(IntVar())
            Label(frame43, text="         "+personnage.competence(i, 2)+':')\
                .grid(row=i-35, column=0, sticky='E')
            Entry(frame43, textvariable=self.Entry_A[i], justify='right', width=3)\
                .grid(row=i-35, column=1, sticky='W', padx="5")
        Label(frame43, text=' ').grid(row=7, column=0, sticky='E')

        # Colonne 3 : Draconic
        self.Draconic = []
        for i in range(0, 4):
            self.Entry_A.append(IntVar())
            Label(frame44, text="             "+personnage.competence(i+42, 2)+':')\
                .grid(row=i, column=0, sticky='E')
            self.Draconic.append(Entry(frame44, textvariable=self.Entry_A[i+42], justify='right', width=3))
            self.Draconic[i].grid(row=i, column=1, sticky='W', padx="5")
        Label(frame44, text=' ').grid(row=4, column=0, sticky='E')

        # Colonne 4 : Combat Mélée
        for i in range(46, 59):
            self.Entry_A.append(IntVar())
            Label(frame45, text=personnage.competence(i, 2) + ':') \
                .grid(row=i - 46, column=0, sticky='E')
            Entry(frame45, textvariable=self.Entry_A[i], justify='right', width=3) \
                .grid(row=i - 46, column=1, sticky='W', padx="5")
        for i in range(13, 15):
            Label(frame45, text=' ').grid(row=i, column=0, sticky='E')

        # Colonne 5 : Combat Tir
        for i in range(59, 65):
            self.Entry_A.append(IntVar())
            Label(frame46, text="         " + personnage.competence(i, 2) + ':') \
                .grid(row=i - 59, column=0, sticky='E')
            Entry(frame46, textvariable=self.Entry_A[i], justify='right', width=3) \
                .grid(row=i - 59, column=1, sticky='W', padx="5")
        for i in range(6, 15):
            Label(frame46, text=' ').grid(row=i, column=0, sticky='E')

        # frame5 : table de résolution et lancer de dé
        frame5 = LabelFrame(root, text=" Résolution et Lancer de Dés ", borderwidth=2, relief='ridge', height=200, width=600)
        frame5.grid(row=0, column=1, rowspan=3, columnspan=2, sticky='NW', padx="10", pady="5")

        # Listbox caractéristiques
        Label(frame5, text='Caractéristique:').grid(row=0, column=0, sticky='NE')
        self.liste1 = Listbox(frame5, height=13, width=16, relief='sunken')
        self.liste1.grid(row=0, column=1, sticky='NW', padx="10", pady="5")
        for i in range(0, 18):
            self.liste1.insert(i, personnage.caracteristique(i, 1))
        self.liste1.bind('<<ListboxSelect>>',self.sel_liste1)

        # Listbox compétences
        Label(frame5, text='Compétence:').grid(row=0, column=2, sticky='NE')
        self.liste2 = Listbox(frame5, height=13, width=16, relief='sunken')
        self.liste2.grid(row=0, column=3, sticky='NW', padx="10", pady="5")
        for i in range(0, 46):
            self.liste2.insert(i, personnage.competence(i, 2))
        self.liste2.bind('<<ListboxSelect>>', self.sel_liste2)

        # Zone de résulats
        Label(frame5, text=' ').grid(row=16, column=0, sticky='NE')
        self.Entry_R_C_Val = IntVar()
        Entry(frame5, textvariable=self.Entry_R_C_Val, justify='right', width=3, state='disabled') \
            .grid(row=17, column=0, sticky='E', padx="10")
        self.Entry_R_C_Name = StringVar()
        Entry(frame5, textvariable=self.Entry_R_C_Name, justify='left', width=16, state='disabled') \
            .grid(row=17, column=1, sticky='W', padx="10")
        self.Entry_R_A_Val = IntVar()
        Entry(frame5, textvariable=self.Entry_R_A_Val, justify='right', width=3, state='disabled') \
            .grid(row=17, column=2, sticky='E', padx="10")
        self.Entry_R_A_Name = StringVar()
        Entry(frame5, textvariable=self.Entry_R_A_Name, justify='left', width=16, state='disabled') \
            .grid(row=17, column=3, sticky='W', padx="10")
        Label(frame5, text='   Seuil de Réussite:').grid(row=18, column=0, sticky='NE')
        self.Entry_R_Seuil = IntVar()
        Entry(frame5, textvariable=self.Entry_R_Seuil, justify='right', width=3, state='disabled')\
            .grid(row=18, column=1, sticky='W', padx="10")
        Label(frame5, text='Tirage:').grid(row=18, column=2, sticky='NE')
        self.Entry_R_Tirage = IntVar()
        Entry(frame5, textvariable=self.Entry_R_Tirage, justify='right', width=3, state='disabled') \
            .grid(row=18, column=3, sticky='W', padx="10")
        Label(frame5, text='Résultat Spécial:').grid(row=19, column=0, sticky='NE')
        self.Entry_R_Special = StringVar()
        Entry(frame5, textvariable=self.Entry_R_Special, justify='left', width=30, state='disabled') \
            .grid(row=19, column=1, columnspan=2, sticky='W', padx="10")
        Label(frame5, text=' ').grid(row=20, column=0, sticky='NE')

        # Bouton pour le lancer de Dés
        Button(frame5, text="Lancer les Dés", command=self.lancer) \
            .grid(row=19, column=3, columnspan=3, sticky='W', padx="10")

        # La mascote
        # On la fait déborder sur le frame4 pour gagner en largeur totale
        self.dragon = PhotoImage(file='./dragon3.gif')
        logo = Canvas(root, width=200, height=181, bd=1, relief='ridge')
        logo.grid(row=3, column=1, columnspan=2, sticky='SE', padx="10", pady="4")
        logo.create_image(0, 0, image=self.dragon, anchor='nw')

        # L'ecran étant initialisé, on peut créér un premier personnage par défaut
        self.creer()
        return

    # Callback de recopie de la sélection depuis la Listbox des caractéristiques
    # Met à jour les 2 champs points et nom de caractéristique pour le calcul de résolution
    def sel_liste1(self, event):

        if self.liste1.curselection() != ():
            index = self.liste1.curselection()[0]
            self.Entry_R_C_Name.set(self.liste1.get(index))
            self.Entry_R_C_Val.set(self.Entry_C[index].get())
        return

    # Callback de recopie de la sélection depuis la Listbox des compétences
    # Met à jour les 2 champs points et nom de compétence pour le calcul de résolution
    def sel_liste2(self, event):

        if self.liste2.curselection() != ():
            index = self.liste2.curselection()[0]
            self.Entry_R_A_Name.set(self.liste2.get(index))
            self.Entry_R_A_Val.set(self.Entry_A[index].get())
        return

    # Callback de changement d'etat haut-rêvant
    def sel_revant(self):

        if self.Entry_HRevant.get() != 1:
            for i in range(0, 4):
                self.Entry_A[i+42].set(-11)
                self.Draconic[i].configure(state='disabled')
        else:
            for i in range(0, 4):
                self.Draconic[i].configure(state='normal')
        return

    # Nouveau jeu
    # Il faut préalablement fermer le jeu en cours
    def nouveau(self):

        if self.fermer():
            self.jeu.nouveau()
        return

    # Ouvrir jeu
    # Il faut préalablement fermer le jeu en cours
    # On reçoit le nom du jeu suivi d'une liste de personnages ou None si rien d'ouvert par le jeu
    def ouvrir(self):

        if self.fermer():
            names = self.jeu.ouvrir()
            if names != None:
                index = -1
                for person in names:

                    # index 0 : nom du fichier jeu
                    if index < 0:
                        self.root.title('Rêve de Dragon - ' + person)

                    # autres index : personnages
                    # index vaudra le nombre de personnages reçus
                    else:
                        self.viewmenu.add_command(label=person, command=lambda index=index: self.selectionner(index))
                    index += 1

                # On affiche le premier personnage
                if index > 0:
                    self.selectionner(0)

        return

    # Fermer le jeu en cours
    # On efface tous les personnages
    # on cree un nouveau personnage vide pour obtenir un affichage vierge
    def fermer(self):

        if not self.saved:
            self.saved = askyesno('Fermer', 'Voulez-vous vraiment fermer ce Jeu ?\nLes données non enregistrées seront perdues')
        if self.saved:
            last = self.viewmenu.index("end")
            if last is not None:
                for i in range(last + 1):
                    self.viewmenu.delete(0)
            self.root.title('Rêve de Dragon')
            self.jeu.fermer()
            self.creer()
        return self.saved

    # Quitter le programme
    # onh détruit la fenêtre et on quitte
    def quitter(self):

        if askyesno('Quitter', 'Voulez-vous vraiment quitter le programme ?'):
            self.root.destroy()
            self.root.quit()
        return

    # Fonction interne d'affichage des données d'un personnage
    # Copie toutes les données du dictionnaire local dans les variables associées aux champs de saisie
    def affiche(self):

        self.Entry_Nom.set(self.pod["Fiche"]["Nom"])
        self.Entry_Age.set(self.pod["Fiche"]["Age"])
        self.Entry_Taille.set(self.pod["Fiche"]["Taille"])
        self.Entry_Poids.set(self.pod["Fiche"]["Poids"])
        self.Entry_Sexe.set(self.pod["Fiche"]["Sexe"])
        self.Entry_Cheveux.set(self.pod["Fiche"]["Cheveux"])
        self.Entry_Yeux.set(self.pod["Fiche"]["Yeux"])
        self.Entry_Beaute.set(self.pod["Fiche"]["Beaute"])
        self.Entry_Ambidextre.set(self.pod["Fiche"]["Ambidextre"])
        self.Entry_HRevant.set(self.pod["Fiche"]["Haut_Revant"])
        self.Entry_SignesP.set(self.pod["Fiche"]["Signes_Particulier"])
        for i in range(0, 18):
            self.Entry_C[i].set(self.pod["Caracteristique"][personnage.caracteristique(i, 0)])
        for i in range(0, 7):
            self.Entry_P[i].set(self.pod["Point"][personnage.point(i, 0)])
        for i in range(0, 65):
            self.Entry_A[i].set(self.pod["Competence"][personnage.competence(i, 0)][personnage.competence(i, 1)])
        if self.Entry_HRevant.get() != 1:
            for i in range(0, 4):
                self.Draconic[i].configure(state='disabled')
        return

    # Création d'un nouveau personnage
    # On demande au jeu de créer un nouveau personnage dans la liste
    # On initialise toutes les variables de saisie aux valeur reçues
    def creer(self):

        self.pod = self.jeu.creer()
        self.affiche()
        return

    # Validation des données du personnage
    # On reconstitue le dictionnaire qui est envoyé au jeu pour vérification
    # Le jeu répond avec un dictionnaire contenant
    # - l'index du personnage
    # - Le nom de personnage
    # - Un message d'erreur ou d'acceptation
    def valider(self):

        if len(self.Entry_Nom.get()) < 1:
            return

        self.pod["Fiche"]["Nom"] = self.Entry_Nom.get()
        self.pod["Fiche"]["Age"] = self.Entry_Age.get()
        self.pod["Fiche"]["Taille"] = self.Entry_Taille.get()
        self.pod["Fiche"]["Poids"] = self.Entry_Poids.get()
        self.pod["Fiche"]["Sexe"] = self.Entry_Sexe.get()
        self.pod["Fiche"]["Cheveux"] = self.Entry_Cheveux.get()
        self.pod["Fiche"]["Yeux"] = self.Entry_Yeux.get()
        self.pod["Fiche"]["Beaute"] = self.Entry_Beaute.get()
        self.pod["Fiche"]["Ambidextre"] = self.Entry_Ambidextre.get()
        self.pod["Fiche"]["Haut_Revant"] = self.Entry_HRevant.get()
        self.pod["Fiche"]["Signes_Particulier"] = self.Entry_SignesP.get()
        for i in range(0, 18):
            self.pod["Caracteristique"][personnage.caracteristique(i, 0)] = self.Entry_C[i].get()
        for i in range(0, 7):
            self.pod["Point"][personnage.point(i, 0)] = self.Entry_P[i].get()
        for i in range(0, 65):
            self.pod["Competence"][personnage.competence(i, 0)][personnage.competence(i, 1)] = self.Entry_A[i].get()
        retour = self.jeu.valider(self.pod)
        index = retour["index"]

        # On a bien un index valide : alors on met à jour le menu et on va chercher les données du personnage
        if index is not None:
            if self.viewmenu.entrycget(index, 'label') != self.Old_Nom:
                self.viewmenu.entryconfigure(index, label=retour["nom"])
            elif self.viewmenu.entrycget(index,'label') != retour["nom"]:
                self.viewmenu.add_command(label=retour["nom"], command=lambda index=index: self.selectionner(index))
            self.pod = self.jeu.selectionner(index)
            self.affiche()

        # En cas d'erreur ou retour ok, il y a un message du jeu
        if len(retour["message"]):
            showerror("Validation", retour["message"])

        self.saved = False
        return

    # Sélection d'un personnage depuis le menu
    # On envoie au jeu l'index du menu qui correspond à l'index de la liste du jeu
    # Les données du personnage reçu sont ensuite affichées
    def selectionner(self, code):

        self.pod = self.jeu.selectionner(code)
        self.affiche()
        return

    # Nouvelle partie
    # On demande au Jeu de changer de partie
    # Le jeu renvoie le contenu du personnage courant
    def partie(self):

        if askyesno('Nouvelle Partie', 'Voulez-vous vraiment terminer cette partie ?\nLes données non enregistrées seront perdues'):
            self.pod = self.jeu.partie()
            self.affiche()
        return

    # Lancer de dé
    # !!! trouver un moyen de verrouiller la fonction si pas ok pour lancer
    # !!!
    # Calcul de résolution puis lancer des dés
    def lancer(self):

        resultat = self.jeu.lancer(self.Entry_R_C_Val.get(),self.Entry_R_A_Val.get())
        self.Entry_R_Seuil.set(resultat["seuil"])
        self.Entry_R_Tirage.set(resultat["tirage"])
        self.Entry_R_Special.set(resultat["special"])
        self.saved = False
        return

    # Affichage de la boite de dialogue A propos
    # Le texte est dans le fichier A_PROPOS.TXT
    def a_propos(self):

        fp = open("A_PROPOS.TXT", "r")
        texte_a_propos = fp.read()
        fp.close()
        showinfo("A Propos de...", texte_a_propos)
        return

    # Dialogue d'aide pour connaitre les règles du jeu
    # Le texte est dans le fichier REGLES.TXT
    def regles(self):

        file = "REGLE.TXT"
        titre = "Règles du Jeu Rêve de Dragon."
        self.aide(file,titre)
        return

    # Le texte est dans le fichier AIDE.TXT
    def utilise(self):

        file = "AIDE.TXT"
        titre = "Utilisation de Rêve de Dragon."
        self.aide(file,titre)
        return

    # Aide du jeu
    # Affiche une boite de dialogue avec un widget texte contenant l'aide
    def aide(self, file, titre):

        # On ouvre une fenêtre fille de celle du jeu
        self.wdw = Toplevel()
        self.wdw.geometry('+400+100')
        self.wdw.title(titre)

        # Le texte de l'aide est stocké dans un fichier Atexte
        fp = open(file, "r")
        texte_aide = fp.read()
        fp.close()

        # On l'affiche dans un widget Text avec une barre de défilement
        # Ne fonctionne que si on utilise grid pour placer les Widgets
        # Il faut mettre le widget en état disabled pour éviter que l'on y entre du texte
        self.S = Scrollbar(self.wdw, orient='vertical')
        self.T = Text(self.wdw, height=50, width=100, font=('TkDefaultFont',10))
        self.T.grid(row=0, column=0, sticky='NW')
        self.S.configure(command=self.T.yview)
        self.T.configure(yscrollcommand=self.S.set)
        self.S.grid(row=0, column=1, sticky='SN')
        self.T.configure(state='normal')
        self.T.insert('end', texte_aide)
        self.T.configure(state='disabled')

        # La nouvelle fenêtre est ouverte en modal
        # Il faudra la fermer pour reprendre le contrôle de la fenêtre principale
        self.wdw.transient(self.root)
        self.wdw.grab_set()
        self.root.wait_window(self.wdw)
        return

    # fonction qui ne fait rien (pour les tests)
    def void(self):
        return