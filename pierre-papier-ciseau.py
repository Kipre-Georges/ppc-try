from random import *
import random

pi="pierre"
pa="papier"
ci="ciseau"


print("Bienvenue dans le jeu de pierre, papier, ciseau")
print("choisissez 1 pour la pierre")
print("choisissez 2 pour le papier")
print("choisissez 3 pour le sciseau")

choix=int(input("Saisissez votre choix : "))

if choix ==1:
    print("vous avez choisit : la pierre")
    choix_ia=[pi,pa,ci]
    choix_final=(random.choice(choix_ia))
    print ("L'ia a choisit : ",choix_final)
    
    if choix_final==pa:
        print (" l'ia a gagner ")
    
    if choix_final==ci:
        print(" Vous avez gagner ")

    if choix_final==pi:
        print(" égalité ")

if choix ==2:
    print(" Vous avez choisit la papier ")
    choix_ia=[pi,pa,ci]
    choix_final=(random.choice(choix_ia))
    print("l'ia a choisit : ",choix_final)

    if choix_final==pa:
        print(" égalité ")

    if choix_final==ci:
        print("l'ia a gagner : ")
    
    if choix_final==pi:
        print(" Vous avez gagner ")

if choix ==3:
    print ("vous avez choisit le sciseau")
    choix_ia=[pi,pa,ci]
    choix_final=(random.choice(choix_ia))
    print("l'ia a choisit : ",choix_final)

    if choix_final==pa:
        print("Vous avez gagner")
    
    if choix_final==ci:
        print("égalité")

    if choix_final==pi:
        print(" l'ia a gagner ")