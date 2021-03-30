#################################
# Ex6: tentative(s) d’authentification illimitées
# 20205793 Rouba Rizkallah
# Créé le 10/03/2021
################################

import stdiomask 
#importe le module stdiomask qui permet de remplacer la valeur saisie par des etoiles

def Authentification():
#fonction Authentification qui ne prend aucun paramètre 
    n_pass=n_id=0
#initialisation a 0 des variables de decompte des tentatives pour le mot de passe et l'identifiant
    id_valide=20205793
    pass_valide=2002
#variables contenant les valeurs de l'identifiant et du mot de passe de verification
    print("Veuillez saisir votre identifiant, vous disposez de 3 tentative(s):")
    id_saisi = int(input("Identifiant:"))
    print("Veuillez saisir votre mot de passe, vous disposez de 3 tentative(s):")
    pass_saisi = int(stdiomask.getpass("Mot de passe:"))
#emploi du module stdiomask
#masque le mot de passe entré en le remplacant par des etoiles
#demande a l'utilisateur son identifiant et son mot de passe en le prevennat qu'il ne dispose que de 3 tentatives pour chacun
#Puis les convertit en valeurs entieres pour pouvoir les comparer aux valeurs valides
    
    if id_saisi == id_valide and pass_saisi == pass_valide :
        print("Votre identifiant et votre mot de passe sont valides.")
#alerte l'utilisateur que son id et son mot de passe sont corrects

  
    while (id_saisi != id_valide and n_id<3) or (pass_saisi!=pass_valide and n_pass<3):
#boucle while declenchee par l'une des 2 doubles conditions:
#soit le mot de passe est invalide et le nombre de tentatives effectuées du mot de passe n_pass est inférieur a 3
#soit l'identifiant est invalide et le nombre de tentatives effectuées de lidentifiant n_id eat inf a 3
        pass_restant = str(3-n_pass)
        id_restant = str(3-n_id) 
#les variables pass_restant et id_restant stockent le nombre de tentatives restantes au type chaine de caracteres

        if id_saisi == id_valide and pass_saisi != pass_valide:
            n_pass+=1 
#incremente la valeur de n_pass de 1 si la saisie du mot de passe est incorrecte            
            print("\nVotre mot de passe est invalide.\nVeuillez resaisir votre mot de passe, il ne vous reste plus que " + pass_restant +" tentative(s):")
            pass_saisi = int(stdiomask.getpass("Mot de passe:"))
            if pass_saisi==pass_valide :
                print("\nVotre mot de passe est valide!")
#alerte  l'utilisateur que son mpt de passe est incorrect et lui demande de le resaisir
#puis l'infrome lorsque l'entree est correcte

        elif id_saisi != id_valide and pass_saisi == pass_valide:
            n_id +=1
#incremente la valeur de n_id de 1 si la saisie de l'id est incorrecte
            print("\nVotre identifiant est invalide.\nVeuillez resaisir votre identifiant, il ne vous reste plus que " + id_restant +" tentative(s):") 
            id_saisi = int(input("Identifiant:"))

            if id_saisi==id_valide :
                print("\nVotre identifiant est valide!")
#alerte l'utilisateur que son id est incorrect et lui demande de le resaisir 
#puis l'infrome lorsque l'entree est correcte

        else:
            n_id+=1
            n_pass+=1
#incremente la valeur de n_id et n_pass de 1 si la saisie du mot de passe et de l'identifiant sont incorrects
            print("\nVotre identifiant et votre mot de passe sont invalides.\nVeuillez les resaisir, il ne vous reste plus que " + id_restant +" tentative(s):")
            id_saisi = int(input("Identifiant:"))
            pass_saisi = int(stdiomask.getpass("Mot de passe:"))

            if pass_saisi==pass_valide :
                print("\nVotre mot de passe est valide!")
            elif id_saisi==id_valide :
                print("\nVotre identifiant est valide!")
            else:
                pass

       
#alerte l'utilisateur que son id et son mot de passe sont incorrects et lui demande de les resaisir            
#puis l'infrome lorsque l'entree est correcte            
            
#Boucle while permettant 3 tentatives en cas d'un mot de passe incorrect et 3 tentatives pour un identifiant incorrect
#Cela en incrementant de 1 n_id lorsque l'identifiant est incorrect et n_pass de 1 lorsque le mot de passe est incorrect
#la condition de la boucle n'est plus valide lorsque n_id et n_pass atteignent la valeur 3

    
Authentification()




    






