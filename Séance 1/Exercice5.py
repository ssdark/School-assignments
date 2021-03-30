#################################
# Ex5 : Autorisation d’accès
# 20205793 Rouba Rizkallah
# Créé le 10/03/2021
#################################

#Note au correcteur:Veuillez excuser l'absence d'accents, mon clavier est un qwerty et c'est assez couteux de mon temps de devoir switcher entre qwerty et azerty

import stdiomask 
#importe le module stdiomask qui permet de remplacer la valeur saisie par des etoiles

def Authentification():
#fonction Authentification qui ne prends aucun paramètre 
    id_valide=20205793
    pass_valide=2002
    print("Veuillez saisir votre identifiant:")
    id_saisi = int(input("Identifiant:"))
    print("Veuillez saisir votre mot de passe:")
    pass_saisi = int(stdiomask.getpass("Mot de passe:"))
#emploi du module stdiomask
#masque le mot de passe entré en le remplacant par des etoiles
#demande a l'utilisateur son identifiant et son mot de passe 
#Puis les converties en valeurs entieres pour pouvoir les comparer aux valeurs valides
 

    if id_saisi == id_valide and pass_saisi == pass_valide :
        print("Votre identifiant et votre mot de passe sont valides")
#informe l'utilisateur que son id et son mot de passe sont corrects
    elif id_saisi == id_valide and pass_saisi != pass_valide:
        print("Votre mot de passe est invalide")
#alerte  l'utilisateur que son mot de passe est incorrect
    elif id_saisi != id_valide and pass_saisi == pass_valide:
        print("Votre identifiant est invalide") 
#alerte l'utilisateur que son id est incorrect
    else:
        print("Votre identifiant et votre mot de passe sont invalides")
#alerte l'utilisateur que son id et son mot de passe sont incorrects
#verification de la validite du mot de passe et de l'identifiant et affichage d'une message en fonction de chaque cas

        
Authentification()




    