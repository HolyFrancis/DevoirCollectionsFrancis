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
print("ajouter un element à la fin de la liste\n\n")
listes.append("Samuel")
print(listes,"\n")



