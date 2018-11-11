#!/usr/bin/python3.4
#1b-dic.py
#entrée utilisateur
#LESPRIT Jérémy
#16/10/2018

list=[]
while 1:
	entreeprenom=input("Entrez un prénom et q pour quitter: ")
	if entreeprenom=="q":
  		break
	else: 
  		list.append(entreeprenom)
list.sort()
print(list)
