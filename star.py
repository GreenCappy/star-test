import sys

# J'ai ajouté des espaces pour les étoiles de taille 1 car ils ne fonctionnaient pas,
# même si toutes les autres tailles fonctionnaient.

def genStar(size):

    star = ""


    # L'étoile ne peut pas avoir une taille négative ou nulle
    if (size>0):


        # 1e partie : triangle
        for x in range(size):
            for y in range(size*3-1-x):
                star += " "
            # Pour que l'étoile de taille 1 ressemble quand même à une étoile.
            if (size==1):
                star += " "
            star += "*"

            for y in range(2*x-1):
                star += " "
            if (x!=0):
                star += "*"

            star += "\n"

        # 2e partie : ligne
        # ligne
        for x in range(size*2+1):
            star += "*"
        #courbe en haut
        for x in range(size*2-3):
            star += " "
        
        # Pour que l'étoile de taille 1 ressemble quand même à une étoile.
        if (size==1):
            star += " "

        for x in range(size*2+1):
            star += "*"
        star += "\n"


        # 3e partie : courbe décroissante
        for x in range(size):
            for y in range(x+1):
                star += " "
            star += "*"
            #On prend en variable la somme de la ligne entière d'avant et on y soustrait la variable à incrémenter
            #(size*2+1+size*2-3+size*2+1-x-3-x-1)

            for z in range(6*size-2*x-5):
                star += " "

            # Pour que l'étoile de taille 1 ressemble quand même à une étoile.
            if (size==1):
                star += " "
                star += " "

            star += "*"

            star += "\n"



        # 4e partie : courbe croissante
        for x in range(size-1):
            for y in range(size-x-1):
                star += " "
            star += "*"
            #variable de ligne et courbe ensemble! mais on soustrait 2
            #((size+2+size*2+size*2)+2*x-2-size-1)
            for x in range(4*size+2*x-1):
                star += " "


            star += "*"

            star += "\n"
        



        # 5e partie : ligne

        for x in range(size*2+1):
            star += "*"
        #courbe en haut
        for x in range(size*2-3):
            star += " "
        # Pour que l'étoile de taille 1 ressemble quand même à une étoile.
        if (size==1):
            star += " "
        for x in range(size*2+1):
            star += "*"
        star += "\n"



        # 6e partie : triangle
        for x in range(size):
            for y in range(x+size*2):
                star += " "
            # Pour que l'étoile de taille 1 ressemble quand même à une étoile.
            if (size==1):
                star += " "
            star += "*"

            for y in range(2*(size-x)-3):
                star += " "
            if (x<size-1):
                star += "*"
            star += "\n"
    return star


# Pour les arguments entrés dans la ligne de commande
if (len(sys.argv)!=2):
    # dans le retour des erreurs
    sys.stderr.write("Usage: python ./star.py\n")
else:
    sizeInput = sys.argv[1]

    try:
        # si c'est pas un entier
        size = int(sizeInput)

        # si c'est négatif
        if (size<0):
            sys.stderr.write("Usage: python ./star.py\n")
        # si tout est bon
        else:
            star = genStar(size)
            print(star)
    except:
        sys.stderr.write("Usage: python ./star.py\n")

