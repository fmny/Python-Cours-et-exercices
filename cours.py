# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 18:43:44 2021

@author: francis
"""

#Lien du cours: https://python.sdv.univ-paris-diderot.fr/

#################################################################
#Chapitre 2-VARIABLES
#################################################################
#Exemple d'écriture d'un nombre le "_" permet de faire office de séparateur de millier
humans_on_earth = 7_807_568_245
humans_on_earth
#7807568245

#puissance: 2^3
2**3

#opérateur
i=0
i+=5
i
#i=5

i*=5
i
#i=25

####################################################
#Opération sur les chaîne de caractère
####################################################

chaine = " Salut "
chaine
#Salut
chaine + " Python "
#'Salut Python '
chaine * 3
#' Salut Salut Salut '

#FonctionType()
x=1
type(x)
#int

y=1.0
type(y)

z='bonjour'
type(z)

#Conversion de types
#fonction int(), float(), str()
i=3
type(i)

str(i)
#'3'

#################################################################
#Chapitre 3-AFFICHAGE (la fonction print()
#################################################################

#utilisaton de la fonction print
print ("Hello") ; print ("Joe")
#Hello
#Joe
print ("Hello", end ="") ; print ("Joe")
#HelloJoe
print ("Hello", end =" ") ; print ("Joe")
#Hello Joe


x = 32
nom = "John"
print ( nom , "a", x ,"ans")
#John a 32 ans
#la "," insère des espaces
#on peut changer cela

x = 32
nom = "John"
print ( nom , "a", x , "ans", sep ="")

print ( nom , "a", x , "ans", sep ="-")

#concaténation chaîine de caractères
ani1 = "chat"
ani2 = "souris"
print ( ani1 , ani2 )
#chat souris
print ( ani1 + ani2 )
#chatsouris
print ( ani1 , ani2 , sep ="")
#chatsouris

#3-2 Ecriture formatée f-string
x = 32
nom = "John"
print (f"{ nom } a {x } ans ")
#John a 32 ans
#l'écriture formatée permet de dire à python qu'entre accolades se trouvent des variables
#on indique à Python qu'il s'agit d'un f-string en mettant 
#un f dans la fonction print()

#si l'on omet le f du f-string
print ("{ nom } a {x} ans ")
#{ nom } a {x} ans

#autres exemples:
var = "to"
print (f"{ var } et { var } font { var }{ var }")

print (f"J' affiche l'entier {10} et le float {3.14}")
#J' affiche l' entier 10 et le float 3.14
print (f"J'affiche la chaine {'Python'}")
#J' affiche la chaine Python

#test FM
s="ma chaîne python"
len(s)
s[0]
#'m'
s[0],s[2],s[3]
#('m', ' ', 'c')


#3-2-3 Spécification de format
#on ne veut afficher que 2 decimales d'un nombre réel

x=0.4780405405405405
#Le résultat obtenu présente trop de décimales (seize dans le cas présent).
#Pour écrire le résultat plus lisiblement, vous
#pouvez spécifier dans les accolades {} le format qui vous intéresse. Dans le cas présent, vous voulez formater un float pour
#l’afficher avec deux puis trois décimales :
print (f"La valeur de x vaut {x:.2f}")

round(x,2)

#mise en forme (attention aux espaces ici)
print (10) ; print (1000)
#10
#1000
print (f"{10: >6d}") ; print (f"{1000: >6d}")
#    10
#  1000
print (f"{10: <6d}") ; print (f"{1000: <6d}")
#10
#1000
print (f"{10:^6d}") ; print (f"{1000:^6d}")
# 10
# 1000
print (f"{10:*^6d}") ; print (f"{1000:*^6d}")
#**10**
#*1000*
print (f"{10:0>6d}") ; print (f"{1000:0>6d}")
#000010
#001000

#> spécifie un alignement à droite, < spécifie un alignement à 
#gauche et ˆ spécifie un alignement centré.


#Ecriture formatée
x = 32
nom = "John"
print ("{} a {} ans ".format(nom,x))
#John a 32 ans 
#f-string est beaucoup plus commode

######################################
#Chapitre 4-Les listes
######################################

#4.1 Définition
#Une liste est une structure de données qui contient une série de valeurs. 
#Python autorise la construction de liste contenant
#des valeurs de types différents (par exemple entier et chaîne de caractères),
# ce qui leur confère une grande flexibilité. Une liste
#est déclarée par une série de valeurs (n’oubliez pas les guillemets, 
#simples ou doubles, s’il s’agit de chaînes de caractères)
#séparées par des virgules, et le tout encadré par des crochets. 
#En voici quelques exemples :
animaux = ["girafe","tigre","singe","souris"]
tailles = [5,2.5,1.75,0.15]
mixte = ["girafe",5,"souris ",0.15]
animaux
#['girafe', 'tigre', 'singe', 'souris']
tailles
[5, 2.5 , 1.75 , 0.15]
mixte
['girafe ', 5, 'souris ', 0.15]

#Lorsque l’on affiche une liste, Python la restitue telle qu’elle a été saisie.

animaux [0]

#4.3 Opération sur les listes

ani1 = ["girafe", "tigre"]
ani2 = ["singe", "souris"]
ani1 + ani2
#['girafe','tigre','singe','souris']
ani1 * 3
#['girafe', 'tigre', 'girafe', 'tigre', 'girafe', 'tigre']


#L’opérateur + est très pratique pour concaténer deux listes.
#Vous pouvez aussi utiliser la méthode .append() lorsque vous souhaitez ajouter un seul 
#élément à la fin d’une liste.
#Dans l’exemple suivant nous allons créer une liste vide :

#Liste vide
a = []
a
#[]
#puis lui ajouter deux éléments, l’un après l’autre, d’abord avec la concaténation :
a = a + [15]
a
#[15]
a = a + [-5]
a
#[15 , -5]
#puis avec la méthode .append() :
a.append (13)
a
#[15 , -5, 13]
a.append ( -3)
a
#[15 , -5, 13 , -3]

#☺4.4 Indiçage négatif
#La liste peut également être indexée avec des nombres négatifs selon le modèle suivant :
#liste :            [" girafe ", " tigre ", " singe " , " souris "]
#indice positif :       0           1           2           3
#indice né gatif :     -4          -3          -2          -1


#Python permet d'utliser les indices positifs et négatifs
ma_liste=[1,2,3,4]
ma_liste
#[1, 2, 3, 4]
ma_liste[-1]
#4
#on obtient le dernier élément de la liste sans connaître forcément sa longueur

#4.5 Tranches
#Un autre avantage des listes est la possibilité de sélectionner une partie d’une liste en 
#utilisant un indiçage construit sur le
#modèle [m:n+1] pour récupérer tous les éléments, du émième au énième 
#(de l’élément m inclus à l’élément n+1 exclu).
ma_liste1=["a","b","c","d","e"]
ma_liste1[0:2]
#['a', 'b'] on a le 0ème élément, le 1er, mais pas le 2e
ma_liste1[0:]
#['a', 'b', 'c', 'd', 'e']
ma_liste1[:]
#['a', 'b', 'c', 'd', 'e']

#On peut aussi préciser le pas en ajoutant un symbole deux-points supplémentaire
# et en indiquant le pas par un entier.

x = [0 , 1, 2, 3, 4, 5 , 6 , 7, 8, 9]
x
#[0 , 1 , 2 , 3 , 4, 5, 6 , 7, 8, 9]
x [::1]
#[0 , 1 , 2 , 3 , 4, 5, 6 , 7, 8, 9]
x[::2]
[0 , 2 , 4 , 6 , 8]
x[::3]
[0 , 3 , 6 , 9]
x[1:6:3]
#[1 , 4]

#4.6 Fonction len()
len(x)
#10

#4.7 Les fonctions range() et list()
#L’instruction range() est une fonction spéciale en Python qui génère des nombres entiers compris dans un intervalle.
#Lorsqu’elle est utilisée en combinaison avec la fonction list(), on obtient une liste d’entiers. Par exemple :
range (10)
#range(0, 10)  
list(range (10))
#[0 , 1 , 2 , 3 , 4, 5, 6 , 7, 8, 9]

#La commande list(range(10)) a généré une liste contenant tous les nombres 
#entiers de 0 inclus à 10 exclu

#on peut ajouter un pas à la fonction range()
list(range (0,1000,200))
#[0, 200, 400, 600, 800]

list(range(10,0,-1))
#[10 , 9, 8, 7, 6, 5, 4, 3, 2, 1]

#4.8 Listes de listes
#Pour finir, sachez qu’il est tout à fait possible de construire des listes de listes. 
#Cette fonctionnalité peut parfois être très pratique. Par exemple :
enclos1 = ["girafe",4]
enclos2 = ["tigre",2]
enclos3 = ["singe",5]
zoo = [enclos1,enclos2,enclos3 ]
zoo
#[[' girafe ', 4] , ['tigre ', 2] , ['singe ', 5]]
#Dans cet exemple, chaque sous-liste contient une catégorie d’animal et le nombre d’animaux 
#pour chaque catégorie.
#Pour accéder à un élément de la liste, on utilise l’indiçage habituel :
zoo [1]
#['tigre ', 2]
#Pour accéder à un élément de la sous-liste, on utilise un double indiçage :
zoo [1][0]
#'tigre '
zoo [1][1]
#2
zoo[0][1]
#4

#4.9 Minimum, maximum et somme d’une liste
#Les fonctions min(), max() et sum() renvoient respectivement le minimum, 
#le maximum et la somme d’une liste passée en argument.
liste = list ( range (10))
liste
#[0 , 1 , 2 , 3 , 4, 5, 6 , 7, 8, 9]
sum ( liste )
#45
min ( liste )
#0
max ( liste )
#test sur des chaînes de caractères
min("a","bb","c")
#'a'
max("a","bb","c")
#'c'

###########################################
#Chapitre 5 - Boucles et comparaisons
##########################################

#5.1 Boucles for

#5.1.1 Principe

animaux = [" girafe ", " tigre ", " singe ", " souris "]
for animal in animaux :
    print ( animal )

for animal in animaux :
    print ( animal )
    print ( animal *2)
print ("C' est fini ")


#5.1.2 Fonction range()

for i in range (4):
     print (i)

list(range (5,10,1))

#5.2 Comparaisons

#Syntaxe Python Signification
#   == égal à
#   != différent de
#   > supérieur à
#   >= supérieur ou égal à
#   < inférieur à
#   <= inférieur ou égal à

#exmples
x = 5
x == 5
#True
x > 10
#False
x < 10
#True

#Dans ce cas, l’ordre alphabétique est pris en compte, par exemple :
"a " < "b"
#True

#5.3 Boucles while

i = 1
while i <= 4:
    print (i)
    i = i + 1

#boucle infinie (on l'arrête par la commande "ctrl+c")
i = 0
while i < 10:
    print (" Le python c' est cool !")
 #   i = i + 1

#while combinée à la fonction input()
i = 0
while i < 10:
    reponse = input (" Entrez un entier supérieur à 10 : ")
    i = int ( reponse )
    
########################################
#Chapitre 6 - Tests
########################################

#test simple
x = 2
#x=3
if x == 2:
    print (" Le test est vrai !")
else : print("le test est faux")    

#test multiple
import random
base = random . choice (["a", "t", "c" , "g"])
print(base)
if base == "a":
    print ("choix d' une adénine")
elif base == "t":
    print ("choix d'une thymine")
elif base == "c":
    print ("choix d' une cytosine")
elif base == "g":
    print ("choix d'une guanine")


#6.3 Importance de l’indentation

#code 1
nombres = [4 , 5, 6]
for nb in nombres :
    if nb == 5:
        print (" Le test est vrai ")
        print (f" car la variable nb vaut { nb }")
#Résultat :
#Le test est vrai
#car la variable nb vaut 5

#Code 2
nombres = [4 , 5, 6]
for nb in nombres :
    if nb == 5:
            print (" Le test est vrai ")
    print (f" car la variable nb vaut { nb }")

#résultat
#car la variable nb vaut 4
#Le test est vrai 
#car la variable nb vaut 5
#car la variable nb vaut 6

#6.4 Tests multiples

x = 2
y = 2
if x == 2 and y == 2:
    print (" le test est vrai ")
#le test est vrai 


x = 2
y = 2
if x == 2:
    if y == 2:
        print (" le test est vrai ")

#le test est vrai 

#6.5 Instructions break et continue

#Ces deux instructions permettent de modifier le comportement d’une boucle (for ou while) 
#avec un test.L’instruction break stoppe la boucle

for i in range (5):
    if i > 2:
        break
    print (i)
#0
#1
#2

#L’instruction continue saute à l’itération suivante, sans exécuter la suite du bloc d’instructions de la boucle.

for i in range (5):
    if i == 2:
        continue
    print (i)

delta = 0.0001
var = 3.0 - 2.7
0.3 - delta < var < 0.3 + delta

abs(var-0.3)< delta

################################
#Chapitre 7
##############################

#Fichiers
#7.1 Lecture dans un fichier

#7.1.1 Méthode .readlines()

#attention à utilisere des "/" et non des "\"
filin=open("C:/Users/Francis/R_new/Python Scripts/Cours Paris 7/zoo.txt","r")
filin
#<_io.TextIOWrapper name='C:/Users/Francis/R_new/Python Scripts/Cours Paris 7/zoo.txt' mode='r' encoding='cp1252'>

filin.readlines()
#['Girafe\n', 'Tigre\n', 'Lion\n', 'Singe']
filin.close()
filin.readlines()
#ValueError: I/O operation on closed file.

path="C:/Users/Francis/R_new/Python Scripts/Cours Paris 7/data/zoo.txt"

filin=open(path,"r")
lignes = filin.readlines()
lignes
#['Girafe\n', 'Tigre\n', 'Lion\n', 'Singe']
for ligne in lignes :
    print(ligne)

filin.close()

#7.1.2 Méthode .read()
with open (path,"r") as filin :
    filin.read()
#ne fait rien ?

#7.2 Écriture dans un fichier
#Écrire dans un fichier est aussi simple que de le lire. Voyez l’exemple suivant :
animaux2 = ["poisson", "abeille", "chat"]
path2="C:/Users/Francis/R_new/Python Scripts/Cours Paris 7/data/"

with open (path2+"zoo2.txt" , "w") as filout :
    for animal in animaux2 :
        filout.write(f"{animal}\n")





