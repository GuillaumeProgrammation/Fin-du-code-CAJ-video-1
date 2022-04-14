#demander le nom
def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
       reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


#demander l'age
def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre age ? ")
        try:
            age_int = int(age_str)
        except:
            print("Erreur, veuillez rentrer un age correct")
    return age_int


#demander nom
nom1 = demander_nom()
nom2 = demander_nom()

#demander l'age
age1 = demander_age(nom1) 
age2 = demander_age(nom2)


#afficher les résultats 
def afficher_information_personne(nom, age, taille=0):
    print()
    print("Vous vous appelez " +  nom + " et vous avez "+ str(age)+ " ans.")
    print("L'an prochain vous aurez " + str(age+1) + " ans.")



#test age (mineur, majeur) avec true/false (Boolean)

#    condition = age >= 18
#   print(condition)
#    print(type(condition))
#    if condition >=18:
#        print("Vous etes majeur.")
#    else:
#        print("Vous etes mineur.")
        
    if age == 17:
        print("Vous etes presque majeur")
    elif 12<= age <18:
        print("Vous etes adolescent")
    elif age == 1 or age  == 2:
        print("Vous etes un bebe")   
    elif age ==18:
        print("Vous etes tout juste majeur : Felicitation")
    elif age > 60:
        print("Vous etes senior")    
    elif age >= 18:
        print("Vous etes majeur.")
    elif age <10:
        print("Vous etes un enfant")    
    else:
        print("Vous etes mineur.")

#renvoie la fonction 
afficher_information_personne(nom1, age1)
afficher_information_personne(nom2, age2)


NB_PERSONNES = 1

#la boucle for
for i in range(0, NB_PERSONNES):
    nom = "personne " + str(i+1)
    age = demander_age(nom)
    afficher_information_personne(nom, age)

print("""
Fin 
De 
La 
Video
""")    










