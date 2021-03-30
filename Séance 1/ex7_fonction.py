import random

classic_sup = ["ensoleillé","pluvieux","nuageux"]
classic_inf = ["pluvieux","nuageux"]
neigeux = ["nuageux","pluvieux","neigeux"]
#initialisation des listes des divers états du ciel

def etat_ciel():
#fonction etat_ciel qui définit l'etat du ciel en fonction de la temperature 
	temp = random.randint(-40, 40)
#la variable temp prend la valeur d'un nombre calcule aleatoirement

	if temp> 8:
		etat = random.choice(classic_sup)
#etat prend une valeur aleatoire de la liste classic_sup si temp est superieur a 8
	elif temp in range (-20,9):
			etat = random.choice(neigeux)
	else :
		etat = random.choice(classic_inf)
#etat prend une valeur aleatoire de la liste:
#classic_sup si la temp est sup a 8
#classic_inf si la temp est inf a 8
#neigeux si la temp est superieure ou egale a -20 et strictement inférieure a 9(inferieure ou egale a 8, les valeurs possibles de temp etant des entiers)

	return etat, temp


def temp_definie(temp):
	
	if temp> 8:
			etat = random.choice(classic_sup)
#etat prend une valeur aleatoire de la liste classic_sup si temp est superieur a 8
	elif temp in range (-20,9):
			etat = random.choice(neigeux)
	else :
		etat = random.choice(classic_inf)
	return etat