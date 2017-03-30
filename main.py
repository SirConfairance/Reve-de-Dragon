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
# main.py
# Corps principal du programme
#
# Crée un objet de type jeu (contenant les règles et le moteur du jeu)
# Crée un objet de type fenetre (contenant l'interface graphique)
# Traite en boucle les évènements de l'interface graphique qui activent les fonctions du jeu
# Le jeu renvoie les valeurs d'affichage vers l'interface graphique

from tkinter import Tk

# Création du jeu
from jeu import Jeu
job = Jeu()

# Création de l'interface graphique

root = Tk()
from fenetre import Fenetre
wnd = Fenetre(root, job)

root.mainloop()