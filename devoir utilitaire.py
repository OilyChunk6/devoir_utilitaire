# AUTEUR : 2232884 2022
# DATE CRÉATION : 2022-12-02 à 10:22

# ALGORYTHME

# LIMITE

# IMPORTS
from utilpy6j5.console import console_utils
from utilpy6j5.math import math_utils
import datetime

# CONSTANTES

# VARIABLES

# LOGIQUE
if console_utils.confirmer():
    print("vous avez confirmé.")
else:
    print("vous n'avez pas confirmé")

réel = console_utils.lire_reel("veuillez saisir un nombre réel")
nb_préféré = console_utils.lire_entier("quel est votre nombre préféré?")
print(nb_préféré)

age = console_utils.lire_entier_intervalle("quel est votre age (3-122)", 3, 122)
print("vous êtes né environ en", datetime.datetime.now().year - age)

nombre: int = int(input("veuillez saisir un nombre"))

est_entier: bool = math_utils.est_premier(nombre)
if est_entier:
    print("ce nombre est entier")
else:
    print("ce nombre n'est pas entier")

est_carré: bool = math_utils.est_carré(nombre)
if est_carré:
    print("ce nombre est est carré")
else:
    print("ce nombre n'est pas carré")

