#################################
# Ex3 : Les 4 opérateurs
# 20205793 Rouba Rizkallah
# Créé le 08/03/2021
#################################
def operations(v,w,x,y,z): #fonction operations qui prend 5 parametres
    if v != 0 :
#s'assure que le denominateur v est non nul avant d'effectuer les operations 
        print(x+y*z-w/v)
    else:
        print("La premiere valeur est le denominateur et ne peut etre nulle.\n" + "Veuillez modifier cette valeur.")

operations(3,2,43,54,5) 
print("\n")
operations(0,42,45,54,32)
print("\r")
operations(-43,-4,-5,-56,-32)
print("\r")
operations(3,-3,-32,-34,43)
print("\r")
operations(-3,0,0,0,0)
print("\r")
