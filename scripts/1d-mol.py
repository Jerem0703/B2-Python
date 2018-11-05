#!/usr/bin/python3.7
#1d-mol.py
#jeu du plus ou moins
#LESPRIT Jérémy 
#23/10/2018

import os
from random import randrange
nombrePropose = 0
nombrealeatoire = randrange(1, 100)
while nombrePropose != nombrealeatoire: 
  print("Quel est le nombre ?")
  nombrePropose = input()
  nombrePropose = int(nombrePropose)
  if nombrePropose < nombrealeatoire:
    print("C'est trop petit !")
  elif nombrePropose > nombrealeatoire:
    print("C'est trop grand !")
  else: 
    print("Bravo, vous avez trouvé le nombre aléatoire !")
