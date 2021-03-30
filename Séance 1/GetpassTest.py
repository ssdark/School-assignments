
'''import stdiomask
import getpass

age = stdiomask.getpass(prompt = 'Enter your age:') #prompt optional to add, works fine without it

print("Entered age is: " + age)


age = getpass.getpass(prompt='Enter your age:')#same for prompt

print("Entered age is: " + age)
man ="Identifiant:"
id_saisi=int(id_saisi[12:])
print(id_saisi)'''



'''n_id =0
id_incorr = False
while n_id<10:
	
	if n_id< 3:
		id_incorr = True
		
	else:
		id_incorr =False
	print(id_incorr)

while (id_saisi != id_valide and n_id<3) or (pass_saisi!=pass_valide and n_pass<3):
        if id_saisi == id_valide and pass_saisi != pass_valide:
            print("Votre mot de passe est invalide.\n Veuillez resaisir votre mot de passe, vous disposez de 3 tentatives:")
            pass_saisi = int(stdiomask.getpass("Mot de passe:"))
            n_pass=+1 
#initialise la valeur de n_id et n_pass a 1 si la saisi du mot de passe et de l'identifiant sont incorrects
#alerte  l'utilisateur que son mpt de passe est incorrect
        elif id_saisi != id_valide and pass_saisi == pass_valide:
            n_id =+1
            id_restant = str(3-n_id)
            print("Votre identifiant est invalide.\n Veuillez resaisir identifiant, il ne vous reste plus que" + id_restant +"tentatives:") 
            id_saisi = int(input("Identifiant:"))
            print(n_id)
            
#initialise la valeur de n_pass a 1 si le mot de passe est incorrect
#alerte l'utilisateur que son id est incorrect
        else:
            print("Votre identifiant et votre mot de passe sont invalides.\n Veuillez les resaisir, vous disposez de trois tentatives pour chacun:")
            id_saisi = int(input("Identifiant:"))
            pass_saisi = int(stdiomask.getpass("Mot de passe:"))
            n_id+=1
            n_pass+=1
            print(n_id) '''

#print(id_incorr)

#incrementation ne fonctionne pas mais fonctionne pour else
import ex7_fonction
nb_jours = 7

for num_jour in range(0,int(nb_jours)):
        num_jour+=1
        #etat,temp1 = ex7_fonction.etat_ciel()
        #etat,temp2 = ex7_fonction.etat_ciel()

        #while temp2 > temp1+10 or temp2 < temp1+10:
           # etat, temp2 = ex7_fonction.etat_ciel()
        #num_jour2=num_jour+1

        #if num_jour != 1:
           # num_jour-=1
        #else:
           # num_jour = num_jour

        print("Dans 1 an et " + str(num_jour) +" jour(s), la température sera de "+"°C avec un ciel ")
        #print("Dans 1 an et " + str(num_jour2) +" jour(s), la température sera de " +str(temp2)+"°C avec un ciel " + etat)
    

#annonce("Rouba")