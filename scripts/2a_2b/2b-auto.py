#!/usr/bin/python3.7
#2a-mol.py
#jeu du plus ou moins automatisé
#LESPRIT Jérémy 
#11/11/2018

from statistics import mean

from 2a_2b.helpers import file_input, print_into_file

MIN, MAX = 0, 100
FILE = "/2a_2b/myfile"


def get_new_proposition(old_proposition, my_answer, mini, maxi):
    assert isinstance(old_proposition, int)
    assert my_answer in ("Trop grand", "Trop petit", "Bravo", "Erreur")


reponse = ''
nombre = mean((MIN, MAX))
print_into_file(FILE, str(round(nombre)))
while True:
    reponse = file_input(FILE, reponse)
    if reponse not in ("Trop grand", "Trop petit", "Bravo", "Erreur"):
        continue
    if reponse == "Trop grand":
        MAX = nombre
    elif reponse == "Trop petit":
        MIN = nombre
    nombre = mean((MIN, MAX))
    if not MIN <= nombre <= MAX:
        raise ValueError
print_into_file(FILE, str(round(nombre)))
