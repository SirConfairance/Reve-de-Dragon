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
# resolution.py
# Fonctions de calcul et de lancer des dés
#
import random

# Fonction de calcul du Seuil de points de 0 à 170
# Ce seuil sera utilisé pour déterminer le succès ou non de l'action en cours pour le personnage
def calcul(caracteristique,competence):

    # On utilise la formule plutôt que le tableau du livre
    return int(caracteristique * (1 + .5 * (competence + 8)))

# Lancer de dés
# On lance 2 dés à 10 faces donnant un résultat entre 1 et 100
def lancer():

    # On lance bien 2 dés
    unit = random.randrange(0, 9)
    dix = random.randrange(0, 9)
    score = 10 * dix + unit

    # Le résultat 0-0 est interprèté comme 100
    if score == 0:
        score = 100
    return score

