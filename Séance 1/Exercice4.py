#################################
# Ex4 : Estimation de l’âge
# 20205793 Rouba Rizkallah
# Créé le 08/03/2021
#################################

#Note au correcteur: ce n'est pas intuitif de rentrer son numero etudiant et sa date de naissance au format chaine de caracteres
###Pour cette raison j'ai considéré que ces deux parametres ont ete definis de type entier 
###Puis j'ai realise les modifications nécessaires dans mon programmes pour travailler avec ces entiers en tant que listes(chaines de caracteres)

def EstimationAge(numero_etudiant,date_naissance):
#fonction EstimationAge qui prend 2 paramètres numero_etudiant et date_naissance

	num_etud = str(numero_etudiant)
	date_naiss = str(date_naissance)
#passage du type entier au type chaine de caractères pour les deux variables numero_etudiant et date_naissance
	if len(num_etud) == 8 and len(date_naiss) == 8:
#verification que la longueur des parametres est de 8 caracteres pour chacun
		num = num_etud[0:4]
		date = date_naiss[0:4]
#transposition des  4 premiers caractères des variables num_etud et date_naiss dans les variables num et date 
		date = int(date)
		num = int(num)
#conversion des variables date et num en entiers pour pouvoir effectuer la soustraction des nbrs
		age = num - date
		return(age)
#retourne l'age de l'utilisateur calcule par la soustraction des 2 variables num et date 
    
	else :
		return(-1)
#si la taille des parametres est differente(souperieur ou inferieur) a 8 ;a fonction retourne -1

print("Entrez votre numero etudiant:") #demande une valeur a l'utilisateur en affichant la phrase entre parentheses
numero_etudiant=input() #lecture de la valeur du numero_etudiant
print("Entrez votre date de naissance au format AAAAMMJJ:") #demande une valeur a l'utilisateur en affichant la phrase entre parentheses
date_naissance=input() #lecture de la valeur du numero_etudiant
#retourne -1 si la longueur des paramètres est différente de 8
print(EstimationAge(numero_etudiant,date_naissance))


     