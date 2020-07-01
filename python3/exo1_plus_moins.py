import random #importer une bibliotheque contenant des fonctions de nombre aleatoire

continuer = "o" # une variable qui nous permet de verifier si on veut ou non continuer
                # par defaut elle est sur o pour oui sinon on ne peut pas rentrer dans la boucle
while(continuer == "o"):
    nb_ordinateur = random.randrange(101) # on genere le nb aleatoire avec la fonction randrange 
                                          # qui se trouve dans la librairie random

    trouver = False # une variable qui nous permet de stocker l'etat de la partie.
                    # True si on a trouver le nb, False si on ne l'a pas encore trouve

    print("Tu dois trouver un nb entre 1 et 100")
    while (trouver == False):
        nb_taper = input(">>") # la fonction input permet de recuperer une valeur tape au clavier
                               # et le stock dans la variable nb_taper sous forme de texte
        nb_taper = int(nb_taper) # ici, on converti nb_taper en nombre entier ( int() ) pour la comparaison plus bas

        if  nb_ordinateur > nb_taper :
            print("Mon nombre est plus grand")
        elif nb_ordinateur < nb_taper:
            print("Mon nombre est plus petit")
        else :
            print("Yolo")
            trouver = True
    
    print("Voulez vous continuer ? o/n")
    continuer = input(">>")