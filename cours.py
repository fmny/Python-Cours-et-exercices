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
print(humans_on_earth)
#7807568245

#puissance: 2^3
print(2**3)

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
#pouvez spécifier dans les accolades {} le format qui vous intéresse. Dans le cas présent, 
#vous voulez formater un float pour
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

###############################################
#Chapitre 8
###############################################

#Modules

#8.1 Définition
#module=librairie

#8.2 Importation de modules
import random
random.randint(0,10)
#10
#je ne comprends pas bien, je pensai qu'en faisant import random, on faisait la même chose que



import math
math.cos(math.pi/2)
#6.123233995736766e-17
math.sin(math.pi/2)
#1.0

from random import *
uniform(0,2.5)
#0.26049637922041596

#il est plus simple d'écrire
import random
random.uniform(0,2.5)
#0.15757543247010952

#Utilisation d' un alias (un nom plus court) pour un module :
import random as rand
rand.randint(1,10)
#6
rand.uniform(1,3)
#2.9063444714055047

#on peut vider la mémoire d'un module
del random
random.randint(0,10)
# File "<ipython-input-11-c21ed48fb247>", line 1, in <module>
#random.randint(0,10)

#NameError: name 'random' is not defined

#8.3 Obtenir de l’aide sur les modules importés

import random
help(random)

help(random.randint)

t = [1 , 2, 3]
help(t)

import random
dir(random)

#8.4 Quelques modules courants
#Il existe une série de modules que vous serez probablement amenés à utiliser si vous programmez en Python. 
#En voici une liste non exhaustive. Pour la liste complète, 
#reportez-vous à la page des modules 4
#sur le site de Python :
#— math : fonctions et constantes mathématiques de base (sin, cos, exp, pi. . . ).
#— sys : interaction avec l’interpréteur Python, passage d’arguments (cf. plus bas).
#— os : dialogue avec le système d’exploitation (cf. plus bas).
#— random : génération de nombres aléatoires.
#— time : accès à l’heure de l’ordinateur et aux fonctions gérant le temps.
#— urllib : récupération de données sur internet depuis Python.
#— Tkinter  : interface python avec Tk. Création d’objets graphiques 
#(cf. chapitre 20 Fenêtres graphiques et Tkinter).
#— re  : gestion des expressions régulières (cf. chapitre 16 Expressions régulières et parsing*).

#8.5 Module random : génération de nombres aléatoires

import random
random.randint(0,10)
#0

random.uniform(0,10)
# 5.4655391640588045

#le module random permet aussi de permuter aléatoirement des listes :
x = [1 , 2, 3, 4]
random.shuffle(x)
x
#[1, 4, 2, 3]

#tirage alétoire d'un ou plusieurs éléments dans une liste donnée :
bases = ["A","T","C","G"]
random.choice(bases)
#'C'

#attention au 's' de choices
random.choices(bases,k=5)
#['C', 'T', 'A', 'T', 'G']

#En Python, la graine aléatoire se définit avec la fonction seed() :
random.seed(42)
random .randint(0,10)
#10
random .randint(0,10)
#10

random.gauss(0,1)
#1.2587003164876114

y=0
for i in range(100):
    x=random.gauss(0,1)
    y=y+x

y/100
#0.11517809397028873
#-0.05416456599684639

#8.6 Module sys : passage d’arguments

#compte ligne

import sys

if len(sys.argv) != 2:
    sys.exit(" ERREUR : il faut exactement un argument .")

nom_fichier =sys.argv[1]
taille = 0
with open (nom_fichier, "r") as f_in :
    taille = len(f_in .readlines())
    print (f"{ nom_fichier } contient { taille } lignes .")

#ces lignes sont reprises dans test.py
import os
os.chdir('C:\\Users\\Francis\\R_new\\Python Scripts\\Cours Paris 7\\data')


runfile('test.py')
#a revoir


#####################################
#Chapitre 9
#####################################

#Fonctions

#9.1 Principe et généralités

#9.2 Définition

def carre(x):
    return x**2

carre(2)
#4

def hello():
    print (" bonjour ")

hello()
#bonjour

#exemple farfelu
var = hello()
#bonjour
print(var)
#None

#reconnaissance des types par python (exemple)
def fois (x , y ):
    return x *y

fois(2,3)
#6
fois (3.1415,5.23)
#16.430045000000003
fois("to",2)
#'toto '
fois ([1,3],2)
#[1 , 3 , 1 , 3]

#9.4 Renvoi de résultats

#Résultats multiples
def carre_cube (x):
    return x**2,x **3

carre_cube(2)
#(4,8)   #tuple, légèrement différent d'une liste

def carre_cube2(x):
    return [x**2,x **3]

carre_cube2(2)
#[4, 8]   #liste

#affectation multiple
z1,z2 =carre_cube2(3)
z1
#9
z2
#27

#valeur par défaut
def fct (x=1):
    return x

fct()
#1

fct(10)
#10

#Mélange aguments positionnels et par défaut
#les arguments positionnels doivent toujours être placés avant les arguments par mot-clé

def fct(a,b,x=0,y=0,z=0):
    return a , b , x , y , z

fct(1,1)
#(1, 1, 0, 0, 0)

fct(1,1,z=5)
#(1, 1, 0, 0, 5)

#pas de val par défaut
def fct2(a,b):
    return a , b 

fct2()
#Traceback (most recent call last):
#  File "<ipython-input-22-9187c07b8cd3>", line 4, in <module>
#    fct2()
#TypeError: fct2() missing 2 required positional arguments: 'a' and 'b'

#test
print(" Message ",end =""),print("toto")
#Out[23]: (None, None)

#9.6 Variables locales et variables globales

#9.7 Principe DRY (dont repeat yourself)
#ne pas dupliquer son code (semble évident, mais pas tant que ça sur des milliers de lignes)

temp_in_fahrenheit = 60

(temp_in_fahrenheit-32)*(5/8)

#la bonne formule est:
(temp_in_fahrenheit-32)*(5/9)
#du coup en la mettant plusieurs fois dans le même programme, 
#il faudrait la changer partout où elle est fausse



################################################
#Chapitre 10
###############################################


#Plus sur les chaînes de caractères

#10.5 Méthodes associées aux chaînes de caractères

x = "girafe"
x.upper ()
#'GIRAFE '
x
#'girafe '
'TIGRE '.lower()
#'tigre '

#Méthode importante: la méthode .split() :
    
animaux = " girafe tigre singe souris "
animaux.split()
#[' girafe ', 'tigre ', 'singe ', 'souris ']

for animal in animaux.split():
    print(animal)

#La méthode .split() découpe une chaîne de caractères en plusieurs éléments 
#appelés champs, en utilisant comme séparateur n’importe quelle
#combinaison « d’espace(s) blanc(s)

#modification de séparateur
animaux = " girafe : tigre : singe :: souris "
animaux.split(":")
#[' girafe ', ' tigre ', ' singe ', '', ' souris ']

#maxsplit
animaux = " girafe tigre singe souris "
animaux.split(maxsplit =1)
#['girafe', 'tigre singe souris ']

#la méthode .find(), quant à elle, recherche une chaîne de 
#caractères passée en argument :
animal = " girafe "
animal.find('i')  #find démarre ici à 1 et non à 0 contrairement au cours (?)
#1

animal.find("afe")
#4
animal.find ("g")
#1
animal.find ("z")
#-1

#méthode replace qui substitue une chaîne de caractères par une autre
animaux = " girafe tigre "
animaux.replace ("tigre", "singe")
#'girafe singe '
animaux.replace ("i", "z")
#gzrafe tzgre

#La méthode .count() compte le nombre d’occurrences 
#d’une chaîne de caractères passée en argument :
animaux = " girafe tigre "
animaux.count("i")
#2

#La méthode .startswith() vérifie si une chaîne de caractères 
#commence par une autre chaîne de caractères :
chaine = " Bonjour monsieur le capitaine !"
chaine.startswith (" Bonjour ")
#True
chaine.startswith ("Bonjour ")
#False


#la méthode .strip() permet de « nettoyer les bords » d’une 
#chaîne de caractères :
chaine = " Comment enlever les espaces au début et à la fin ? "
chaine.strip()
#'Comment enlever les espaces au début et à la fin ?'


#10.6 Extraction de valeurs numériques d’une chaîne de caractères

val ="3.4 17.2 atom "

#On souhaite extraire les valeurs 3.4 et 17.2 pour ensuite les additionner

val2 =val.split()
val2
#['3.4', '17.2', 'atom']

float(val2[0])+float(val2[1])
#20.599999999999998

#10.7 Conversion d’une liste de chaînes de caractères en une chaîne de caractères

seq = ["A","T","G","A","T"]


"-".join(seq)
#'A-T-G-A-T'

"".join(seq)
#'ATGAT'

"@".join(seq)
#'A@T@G@A@T'

#Attention, la méthode .join() ne s’applique qu’à une liste de chaînes de caractères.


#exhaustitivité  des méthodes
animaux = "girafe tigre"
dir(animaux)

#['__add__',
# '__class__',
# '__contains__',
# '__delattr__',
# '__dir__',
#.....

help ( animaux . split )

#Résumé des méthodes
#La méthode .split() découpe une chaîne de caractères

#modification de séparateur
#animaux = " girafe : tigre : singe :: souris "
#animaux.split(":")

#la méthode .find(), quant à elle, recherche une chaîne de caractères

#la méthode .strip() permet de « nettoyer les bords »

#méthode .replace('i','z') par exemple qui substitue une chaîne de 
#caractères par une autre

#.join(sep) Conversion d’une liste de chaînes de caractères 
#en une chaîne de caractères

#Chapitre 11
#Plus sur les listes

#11.1 Méthodes associées aux listes

#11.1.1 .append()

a = [1, 2, 3]
a. append (5)
a
#[1, 2, 3, 5]

#qui est équivalent à :
a = [1, 2, 3]
a = a + [5]
a
#[1, 2, 3, 5]

#Conseil : préférez la version avec .append() qui est plus compacte et facile à lire.

#Conseil : préférez la version avec .append() qui est plus compacte et facile à lire.

#11.1.2 .insert()
#La méthode .insert() insère un objet dans une liste à un indice déterminé :
a = [1, 2, 3]
a.insert (2, -15)


#11.1.3 del
#L’instruction del supprime un élément d’une liste à un indice déterminé :
a = [1, 2, 3]
del a[1]
a
#[1, 3]

#Remarque: Contrairement aux méthodes associées aux listes présentées dans 
#cette rubrique, del est une instruction générale de Python, utilisable 
#pour d’autres objets que des listes. Celle-ci ne prend pas de parenthèse.

#11.1.4 .remove()
#La méthode .remove() supprime un élément d’une liste à partir de sa valeur :
a = [1, 2, 3]
a.remove (3)
a
#[1, 2]


#11.1.5 .sort()
#La méthode .sort() trie les éléments d’une liste du plus petit au plus grand :
a = [3, 1, 2]
a.sort()
a
#[1, 2, 3]

#L’argument reverse=True spécifie le tri inverse, c’est-à-dire du plus grand au plus petit élément :
a = [3, 1, 2]
a.sort(reverse = True)
a
#[3, 2, 1]

#11.1.6 sorted()
#La fonction sorted() trie également une liste. Contrairement à la méthode 
#précédente .sort(), cette fonction renvoie la liste triée et ne modifie 
#pas la liste initiale :
a = [3, 1, 2]
sorted(a)
#[1, 2, 3]
a
#[3, 1, 2]

a = [3, 1, 2]
sorted(a, reverse = True )
#[3, 2, 1]
a
#[3, 1, 2]


#11.1.7 .reverse()
#La méthode .reverse() inverse une liste :
a = [3, 1, 2]
a.reverse ()
a
#[2, 1, 3]

#11.1.8 .count()
#La méthode .count() compte le nombre d’éléments (passés en argument) 
#dans une liste :
a = [1, 2, 4, 3, 1, 1]
a
a.count (1)
#3
a.count (4)
#1
a.count (23)
a

#attention:append(), .sort(), etc.) modifient la liste mais ne renvoient
#rien, c’est-à-dire qu’elles ne renvoient pas d’objet récupérable dans une 
#variable, car la liste a est déjà modifiée "sur place"
a
var = a.reverse()
print(var)
#None






