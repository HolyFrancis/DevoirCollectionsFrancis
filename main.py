
if __name__=='__main__':
    """"
    # I. List of 10 Strings

    #1. creation de la Liste 
    print("1.---------liste de 10 éléments de type chaîne de caractère----------\n")
    listes=['Marc','Jean','Holy','Mike','Jack','Mary','Gilles','Mathiew','Lise','Simon']

    print(listes,"\n\n")

    #2 . changement du contenu de l'element n° 5
    print("2.---------changement du contenu de l'element n° 5-------------\n")
    listes[4]='Jane'

    print(listes,"\n\n")

    # 3. creation d'une list des elements contenant la lettre "a"
    print("3.--------creation d'une list des elements contenant la lettre 'a'---------\n")
    liste_copy=[]
    for list in listes:
        if 'a' in list:
            liste_copy.append(list)

    print(liste_copy,"\n\n")

    #4. ajouter un elemet à la fin de la liste
    print("-----ajouter un element à la fin de la liste\n------")
    listes.append("Samuel")
    print(listes,"\n\n")


    #5. ajout de l'element à l'index n°2
    print("------ajout d'un element à l'index n°2\n------")
    listes.insert(2,'Suzan')
    print(listes,"\n\n")

    # 6. suppression de l'element n°3
    print("------suppression de l'element n°3------\n")
    listes.pop(2)
    print(listes,"\n\n")
    
    # 7. suppression de l'element à l'index n°2
    print("suppression de l'element à l'index n° 2\n")
    listes.pop(2)
    print(listes,"\n\n")
    
    # 8. ordonner la list
    print("-------la liste ordonée--------\n")
    listes.sort()
    print(listes,"\n\n")
    
    # 9. affiche la sens au sens inverse
    print("-----afichage en sen inverse de la liste--------\n")
    listes.reverse()
    print(listes,"\n\n")
    
    # 10 . vider la list
    print("----clear the list-------\n")
    listes.clear()
    print(listes,"\n\n")
    
    # 11. supprime la liste
    del listes
    """
    
    #II
    print("LES TUPLES")
    #1.
    print("-----l'occurence de la valeur '3' dans le tuple----\n")
    tupl=(2,4,3,7,28,18,3,24,3,17)
    print(tupl.count(3),"\n\n")
    
    #2.
    print("----contenu de l'element n°5-----\n")
    print(tupl[4],"\n\n")
    
    #.3 convert the tuple into list for sort the tuple
    print("tuple ordonnéé")
    tu=list(tupl)
    tu.sort()
    print(tu,"\n\n")
    
    #4. append an element to the tuple
    print("ajout d'un element dans le tuple")
    tu.append(20)
    print(tu)
    
    #5. insert on the index 3
    print("------ajout d'un element à l'index 3")
    tu.insert(3,40)
    print(tu)
    