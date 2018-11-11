#!/usr/bin/python3.7
#2a-mol.py
#jeu du plus ou moins dans un fichier 
#LESPRIT Jérémy 
#04/11/2018

from random import randint

from 2a_2b.helpers import print_into_file, file_input


def get_answer(nombreAleatoire, nombrePropose):
    assert isinstance(nombreAleatoire, int)
    assert isinstance(nombrePropose, int)
    if nombreAleatoire == nombrePropose:
        rep = "Bravo"
    elif nombreAleatoire > nombrePropose:
        rep = "Trop grand"
    elif nombreAleatoire < nombrePropose:
        rep = "Trop petit"
    else:
        rep = "Erreur"
    return rep


MIN, MAX = 0, 100
NUMBER = randint(MIN, MAX)
FILE = "2a_2b/myfile"

i = 0
user_input = ''
print_into_file(FILE, user_input)
while True:
    try:
        user_input = int(file_input(FILE, str(user_input)))
    except ValueError:
        continue
    answer = get_answer(user_input, NUMBER)
    i += 1
print_into_file(FILE, answer)
