
#################################
# Ex8:Prévisions climatiques
# 20205793 Rouba Rizkallah
# Créé le 10/03/2021
################################
import ex7_fonction  
#importe le fichier python(module) contenant la fonction de l'exercice 7
print("Entrez votre nom:")
nom = input()

def annonce(nom):
#fonction qui affiche une annonce meteorologique et qui prend en parametre le nom de l'utilisateur
	print("Entrez un nombre de jours supérieur à 1 et inférieur à 356:")
	#Affiche une phrase qui demande a l'utilisateur d'entrer un nombre de jours inferieur au nombre des jours dans une annee
	nb_jours = input()
	#stocke le nombre de jours dans la variable nb_jours

	list_temp = []
	for num_jour in range(0,int(nb_jours)):
		etat,temp = ex7_fonction.etat_ciel()
		list_temp.append(temp)
		
#boucle for qui range les valeurs de la fonction importée etat_ciel() dans la liste list_temp

	for i in range(0,int(nb_jours)):
		while list_temp[i+1]>list_temp[i]+10 or list_temp[i+1]<list_temp[i]-10:
			etat,list_temp[i+1] = ex7_fonction.etat_ciel()
		list_temp.append(list_temp[i+1])
	
#boucle while imbriquee dans une boucle for qui
#reexecute la fonction etat_ciel()
#pour chaque element de la liste list_temp avec un ecart de plus de 10 avec la valeur qui la precede
#La valeur obtenue est ensuite stockee dans list_temp

#################################
# Ex8:Prévisions climatiques
# 20205793 Rouba Rizkallah
# Créé le 10/03/2021
################################

	print("Nombre de jours :\n"+nb_jours+"\nBonjour " +nom+ "," )
#affiche le nombre de jours entrés par l'utilisateur et son nom
	for num_jour in range(0,int(nb_jours)+1):
			temp = list_temp[num_jour]
#stocke dans la variable temp l'element de la liste list_temp d'indexe numero du jour (num_jour)
			etat = ex7_fonction.temp_definie(temp)
#La variable etat prend la valeur de l'etat du ciel donné par la fonctiontemp_definie
#cette fonction temp_definie est identique a la fonction etat_ciel mais prend la temperature en parametre
#cette fonction a donc pour but de donner l'etat du ciel en fonction d'une temperature bien definie
			print("Dans 1 an et " + str(num_jour+1) +" jour(s), la température sera de " +str(temp)+"°C avec un ciel "+ etat)
#boucle for qui repete la phrase a imprimer en faisant varier:
#le numero du jour incremente de 1 etant donne que la premiere valeur de num_jour est 0, num_jour	
#la température, temp	
#et l'état de ciel, etat, en fonction de la temperature

annonce(nom)



	

