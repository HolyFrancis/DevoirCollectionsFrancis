
if __name__=='__main__':
    
    # I. List of 10 Strings

    #1. creation de la Liste 
    print("1.liste de 10 éléments de type chaîne de caractère")
    print("===================================================\n")
    listes=['Marc','Jean','Holy','Mike','Jack','Mary','Gilles','Mathiew','Lise','Simon']

    print(listes,"\n\n")

    #2 . changement du contenu de l'element n° 5
    print("2. changement du contenu de l'element n° 5")
    print("============================================\n")
    listes[4]='Jane'

    print(listes,"\n\n")

    # 3. creation d'une list des elements contenant la lettre "a"
    print("3. creation d'une list des elements contenant la lettre 'a'")
    print("============================================================\n")
    liste_copy=[]
    for l in listes:
        if 'a' in l:
            liste_copy.append(l)

    print(liste_copy,"\n\n")

    #4. ajouter un elemet à la fin de la liste
    print("ajouter un element à la fin de la liste")
    print("======================================\n")
    listes.append("Samuel")
    print(listes,"\n\n")


    #5. ajout de l'element à l'index n°2
    print("ajout d'un element à l'index n°2")
    print("=================================\n")
    listes.insert(2,'Suzan')
    print(listes,"\n\n")

    # 6. suppression de l'element n°3
    print("suppression de l'element n°3")
    print("============================\n")
    listes.pop(2)
    print(listes,"\n\n")
    
    # 7. suppression de l'element à l'index n°2
    print("suppression de l'element à l'index n° 2")
    print("========================================\n")
    listes.pop(2)
    print(listes,"\n\n")
    
    # 8. ordonner la list
    print("la liste ordonée")
    print("=================\n")
    listes.sort()
    print(listes,"\n\n")
    
    # 9. affiche la sens au sens inverse
    print("afichage en sen inverse de la liste")
    print("====================================\n")
    listes.reverse()
    print(listes,"\n\n")
    
    # 10 . vider la list
    print("clear the list")
    print("================\n")
    listes.clear()
    print(listes,"\n\n")
    
    # 11. supprime la liste
    del listes
    
    
    #II
    print("LES TUPLES")
    #1. tuple creation 
    print("l'occurence de la valeur '3' dans le tuple")
    print("==========================================\n")
    tupl=(2,4,3,7,28,18,3,24,3,17)
    print(tupl.count(3),"\n\n")
    
    #2. display n°5 element
    print("contenu de l'element n°5")
    print("========================\n")
    print(tupl[4],"\n\n")
    
    #.3 convert the tuple into list for sort the tuple
    print("tuple ordonnéé")
    print("===============\n")
    tu = list(tupl)
    print(type(tu))
    tu.sort()
    print(tu,"\n\n")
    
    #4. append an element to the tuple
    print("ajout d'un element dans le tuple")
    print("================================\n")
    tu.append(20)
    print(tu)
    
    #5. insert on the index 3
    print("ajout d'un element à l'index 3")
    print("==============================\n")
    tu.insert(3,40)
    print(tu)
    
    #6. affiche la nouvelle tuple
    print("affichage de la nouvelle tuple")
    print("==============================\n")
    #reconvert the list into tuple
    tupl=tuple(tu)
    print(tupl,'\n\n')
    
    
    #III. LES SETS
    #1.set creation
    print("creation et affichage du SET")
    print("=============================\n")
    animaux={'lion','tigre','lapin','bufle','vache','antilope','aigle','poisson','pigeon','mouton'}
    print(animaux,'\n')
    
    #2. add an element
    print("ajout d'un element dans le set")
    print("==============================\n")
    animaux.add('serpent')
    print(animaux,'\n')
    
    #3. remove an element
    print("supression de l'element 'bufle' ")
    print("===============================\n")
    animaux.remove('bufle')
    print(animaux,'\n')
    
    #4. delete the set
    print("suppression de la set")
    print("=====================\n")
    del animaux
    
    
    #IV. DICTIONNAIRE
    #1. dict creation
    print("creation et affichage du dictionnaire")
    print("=====================================\n")
    cours={1:'math',
            2:'francais',
            3:'anglais',
            4:'python',
            5:'java',
            6:'linux',
            7:'mac',
            8:'kiswahili',
            9:'entrepreuneriat',
            10:'algorithmique'
            }
    print(cours,'\n')
    
    #2. affiche les clés
    print("affichage des clés")
    print("==================\n")
    for k in cours.keys():
        print(k,'\n')
    
    #3. affiche les valeurs
    print('affichage des valeurs')
    print('=====================')
    for v in cours.values():
        print(v)
        
    #4. display key and value
    print("\naffiche les cles et valeurs sous le format cle:valeur")
    print("========================================================")
    for key in cours:
        print(key,": ",cours[key])
    
    #5.supprime l'element à la clé n°2
    print("\nsuupression de l'element à la cle n° 2")
    print("=========================================")
    cours.pop(2)
    print(cours)
    
    #6.display n° 5 element
    print("\nAffiche l'élément de la clé numéro 5")
    print("======================================")
    print(cours.get(5))
    
    #7. aad new element
    print("\nAjouter un nouvel élément")
    print("============================")
    cours.setdefault(11,"datamining")
    print(cours)
    
    #8.copy of the dict
    print("\ncreation d'une copie du dictionnaire")
    print("======================================")
    cours_copy=cours.copy()
    print(cours_copy)
    
    
    
    