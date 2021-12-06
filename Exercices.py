# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 15:12:57 2021

@author: Utilisateur
"""

#Exercice du poly cours-python.pdf Paris 7
#Cours de Python
#Introduction à la programmation Python pour la biologie

#Patrick Fuchs et Pierre Poulain


#####################
#Chapitre 3
#####################


#programme pris sur le web
def repeat(word, m, n): 
        
    if(m > len(word)): 
        m = len(word) 
          
    repeat_word = word[:m] 
    result = "" 
      
    for i in range(n): 
        result = result+repeat_word
    return(result)
    print(result) 


#exercice
#répéter une chaîne 20 fois
#penser à mettre un return sinon la fonction ne renvoi rien
#donc le print est bon maiis le type est "none"

#Générez une chaîne de caractères représentant un brin d’ADN poly-A 
#(c’est-à-dire qui ne contient que des bases A) de 20
#bases de longueur, sans taper littéralement toutes les bases.

ma_chaine=repeat("A",1,20)
ma_chaine=str(ma_chaine)
len(ma_chaine)
len("AAA")

####################
#3.6.2 Poly-A
###################
def repeat(word, n): 
                 
    result = "" 
      
    for i in range(n): 
        result = result+word
    return(result)
    print(result)

str1=repeat("A",20)
str1=str(str1)
len(str1)
print(ma_chaine)

#Plus simple
ma_chaine_test="A"*20
ma_chaine_test

########################
#3.6.3 Poly-A et poly-GC
#########################

#Sur le modèle de l’exercice précédent, générez en une ligne de code 
#un brin d’ADN poly-A (AAAA. . . ) de 20 bases suivi
#d’un poly-GC régulier (GCGCGC. . . ) de 40 bases

ma_chaine2=ma_chaine+repeat("GC",40);print(ma_chaine2)


##########################
#3.6.4 Écriture formatée
#########################

#En utilisant l’écriture formatée, affichez en une seule ligne les variables 
#a, b et c dont les valeurs sont respectivement la
#chaîne de caractères "salut", le nombre entier 102 et le float 10.318. 
#La variable c sera affichée avec 2 décimales.

a="salut";b=102;c=10.318;print(f"{a} {b} {c:.2f}")

################################
#3.6.5 Écriture formatée 2
################################

#Dans un script percGC.py, calculez un pourcentage de GC avec l’instruction suivante :
#perc_GC = ((4500 + 2575)/14800)*100
#Ensuite, affichez le contenu de la variable perc_GC à l’écran avec 0, 1, 2 puis 3 décimales sous forme arrondie en utilisant
#l’écriture formatée et les f-strings. On souhaite que le programme affiche la sortie suivante :

#Le pourcentage de GC est 48     %
#Le pourcentage de GC est 47.8   %
#Le pourcentage de GC est 47.80  %
#Le pourcentage de GC est 47.804 %
perc_GC = ((4500 + 2575)/14800)*100

#test 1 (ok mais peu élégant)
print(f"Le pourcentage de GC est {perc_GC:.0f} {'%':>6s}")
print(f"Le pourcentage de GC est {perc_GC:.1f} {'%':>4s}")
print(f"Le pourcentage de GC est {perc_GC:.2f} {'%':>3s}")
print(f"Le pourcentage de GC est {perc_GC:.3f} {'%':>2s}")


##############################################
#Chapitre 4
##############################################

#4.10 Exercices

#4.10.1 Jours de la semaine
#Constituez une liste semaine contenant les 7 jours de la semaine.
ma_liste=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
ma_liste

#1. À partir de cette liste, comment récupérez-vous seulement les 5 premiers jours 
#de la semaine d’une part, et ceux du week-end d’autre part ? Utilisez pour cela l’indiçage.
ma_liste[0:5] #['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
ma_liste[5:7] #['samedi', 'dimanche']

#2. Cherchez un autre moyen pour arriver au même résultat (en utilisant un autre indiçage).
ma_liste[-7:-2] #['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi']
ma_liste[-2:]    #['samedi', 'dimanche']

#3. Trouvez deux manières pour accéder au dernier jour de la semaine.
ma_liste[-1]

ma_liste[6]

#4. Inversez les jours de la semaine en une commande.
ma_liste_inverse=ma_liste[::-1]
ma_liste_inverse
# ['dimanche', 'samedi', 'vendredi', 'jeudi', 'mercredi', 'mardi', 'lundi']


#4.10.2 Saisons
#Créez 4 listes hiver, printemps, ete et automne contenant les mois correspondants à ces saisons. 
#Créez ensuite une liste saisons contenant les listes hiver, printemps, ete et automne. 
#Prévoyez ce que renvoient les instructions suivantes,puis vérifiez-le dans l’interpréteur :
hivers=["janvier","février","mars"]
printemps=["avril","mai","juin"]
ete=["juillet","août","septembre"]
automne=["octobre","novembre","décembre"]

saisons=[hivers,printemps,ete,automne]
saisons
#[['décembre', 'janvier', 'février'],
# ['avril', 'mai', 'juin'],
# ['juillet', 'août', 'septembre'],
# ['octobre', 'novembre', 'décembre']]


#1. saisons[2]
#prévision: [['juillet','août','septembre']] 
#erreur: ['juillet', 'août', 'septembre']
  
#2. saisons[1][0]
#Prévision: 'avril' #ok


#3. saisons[1:2]  prev: 'avril','mai','juin','juillet','août','septembre'
#grosse erreur:[['avril', 'mai', 'juin']]
#logique on ne considère pas l'indice 2 en python (on s'arrêt à 1)

#4. saisons[:][1]. Comment expliquez-vous ce dernier résultat ?
#prev: ['janvier','mai','août','novembre']
saisons[:][1]
#['avril', 'mai', 'juin']

saisons[0][0]
saisons[1][0]
saisons

#extraire le 1er éléments de chaque saison
saisons1=[item[0] for item in saisons]
saisons1

#4.10.3 Table de multiplication par 9
#Affichez la table de multiplication par 9 en une seule commande avec les instructions range() et list().
list(range(0,100,9))
#[0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]

#4.10.4 Nombres pairs
#Répondez à la question suivante en une seule commande. Combien y a-t-il de nombres pairs 
#dans l’intervalle [2, 10000] inclus ?
len(range(2,11,2))
#5

len(range(2,10001,2))
#5000

#test boucle for
for i in range(1,11): print(i)


##############################################
#Chapitre 5
##############################################

#5.4.1 Boucles de base
#Soit la liste ["vache", "souris", "levure", "bacterie"]. Affichez l’ensemble des éléments 
#de cette liste (un élément par ligne) de trois manières différentes 
#(deux avec for et une avec while).

ma_chaine1= ["vache", "souris", "levure", "bacterie"]
for chaine in ma_chaine1:
    print(chaine)

for i in range(len(ma_chaine1)):
    print(ma_chaine1[i])

i=0
while i< len(ma_chaine1):
    print(ma_chaine1[i])
    i=i+1

#5.4.2 Boucle et jours de la semaine
#Constituez une liste semaine contenant les 7 jours de la semaine.
#Écrivez une série d’instructions affichant les jours de la semaine 
#(en utilisant une boucle for), ainsi qu’une autre série
#d’instructions affichant les jours du week-end (en utilisant une boucle while).

semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]

for jour in semaine:
    print(jour)
    
for i in range(len(semaine)):
    print(semaine[i])      

i=0
while i <len(semaine):
    print(semaine[i])
    i=i+1
    
#5.4.3 Nombres de 1 à 10 sur une ligne
#Avec une boucle, affichez les nombres de 1 à 10 sur une seule ligne

for i in range(11):print(i,end=" ")

#5.4.4 Nombres pairs et impairs
#Soit impairs la liste de nombres [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21].
#Écrivez un programme qui, à partir de la liste impairs, construit une liste pairs 
#dans laquelle tous les éléments de impairs sont incrémentés de 1.

impairs=[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

pairs=[]
for nb in impairs:
    pairs=pairs+[nb+1]
print(pairs)

#5.4.5 Calcul de la moyenne
#Voici les notes d’un étudiant [14, 9, 6, 8, 12]. Calculez la moyenne de ces notes. 
#Utilisez l’écriture formatée pour afficher la valeur de la moyenne avec deux décimales.



import statistics

notes=[14, 9, 6, 8, 12]
mean_notes = statistics.mean(notes)
print(mean_notes)
#9.8
print(f"la moyenne vaut {mean_notes}")

#vérification
#(14+9+6+8+12)/5
#9.8

#5.4.6 Produit de nombres consécutifs
#Avec les fonctions list() et range(), créez la liste entiers contenant 
#les nombres entiers pairs de 2 à 20 inclus.
#Calculez ensuite le produit des nombres consécutifs deux à deux de entiers 
#en utilisant une boucle. Exemple pour les premières itérations :
#8
#24
#48
#[...]
pairs2=list(range(2,22,2))
pairs2


for i in pairs2:
    if i <= max(pairs2)-2:
       print(i*(i+2))


#V5.4.7 Triangle
#Créez un script qui dessine un triangle comme celui-ci :
#1 *
#2 **
#3 ***
#4 ****
#5 *****
#6 ******
#7 *******
#8 ********
#9 *********
#10 **********

for i in range(10):
    print((i+1)*"*")
    
#print(5*"*")

#5.4.8 Triangle inversé
for i in range(10):
    print((10-i)*"*")

#5.4.9 Triangle gauche
for i in range(10):
    print((i)*" ",(10-i)*"*")

#5.4.10 Pyramide
#Créez un script pyra.py qui dessine une pyramide comme celle-ci :
#1          *
#2         ***
#3        *****
#4       *******
#5      *********
#6     ***********
#7    *************
#8   ***************
#9  *****************
#10*******************(19 étoiles)
#nb etoiles: 1,3,5,7,9,...,19
#nb espaces: 9,8,7,...,0

for i in range(10):
    print((10-i+1)*" ",(2*i+1)*"*")


reponse = input (" Entrez un nombre de lignes ( entier positif ): ")
N = int ( reponse )

for i in range(N):
    print((N-i+1)*" ",(2*i+1)*"*")
    
    
#5.4.11 Parcours de matrice
#je ne comprends pas

#5.4.13 Sauts de puce (p40)
import random
random.choice([-1,1])

x=0
marche=[]   #je veux sauvegarder ma marche aléatoire entière
while(x<5):
        x=x+random.choice([-1,1])
        marche=marche+[x]
#print(x)
print(marche)

#5.4.14 Suite de Fibonacci (exercice +++)

nterms=15

n1=0
n2=1
print("\n la suite fibonacci est :")
print(n1,", ", n2, end=", ")


for i in range(2, nterms):
  suivant = n1 + n2
  print(suivant, end=", ")
 
  n1 = n2
  n2 = suivant

# Programme pour générer la suite de Fibonacci en utilisant la récursivité
def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Entrez le nombre de termes:"))
print("Suite de Fibonacci en utilisant la recursion :")
for i in range(2,n):
       print(fibonacci(i)," ",{fibonacci(i)/fibonacci(i-1)})
       
#le rapport u(n+1)/u(n) tend vers 1.618034

#print(f"Fibonnacci": {fibonacci(i)}," ","rapport fibo(n+1)/fibo(n)",{fibonacci(i)/fibonacci(i-1)})

#6.7 Exercices

#6.7.1 Jours de la semaine



#En utilisant une boucle, écrivez chaque jour de la semaine ainsi que les messages suivants :
#— Au travail s’il s’agit du lundi au jeudi;
#— Chouette c'est vendredi s’il s’agit du vendredi;
#— Repos ce week-end s’il s’agit du samedi ou du dimanche.

semaine=["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]

for jour in semaine:
    if jour=="lundi"or jour== "mardi" or jour=="mercredi" or jour=="jeudi":
        print("Au travail s’il s’agit du lundi au jeudi")
    elif jour=="vendredi":
        print("Chouette c'est vendredi s’il s’agit du vendredi")
    elif jour=="samedi" or jour=="dimanche": 
        print("Repos ce week-end s’il s’agit du samedi ou du dimanche")

#6.7.2 Séquence complémentaire d’un brin d’ADN
#La liste ci-dessous représente la séquence d’un brin d’ADN :
#["A", "C", "G", "T", "T", "A", "G", "C", "T", "A", "A", "C", "G"]
#Créez un script qui transforme cette séquence en sa séquence complémentaire.
#Rappel : la séquence complémentaire s’obtient en remplaçant A par T, T par A, C par G et G par C.

ADN=["A","C","G","T","T","A","G","C","T","A","A","C","G"]

ADN_comp=[]

for acide in ADN:
    if acide=='A':
        ADN_comp=ADN_comp+['T']
    elif acide=="T":
        ADN_comp=ADN_comp+['A']
    elif acide=="C":
        ADN_comp=ADN_comp+['G']
    elif acide=="G":
        ADN_comp=ADN_comp+['C'] 
        
        
print(ADN_comp)
#['T', 'G', 'C', 'A', 'A', 'T', 'C', 'G', 'A', 'T', 'T', 'G', 'C']

#6.7.3 Minimum d’une liste

nb=[8, 4, 6, 1, 5]
min (nb)

for i in range(len(nb)-1):
    for j in range(len(nb)-1):
        if nb[i]<=nb[j]:x=nb[i]
print(x)
#1

#6.7.4 Fréquence des acides aminés

acide=["A", "R", "A", "W", "W", "A", "W", "A", "R", "W", "W", "R", "A", "G"]
#Calculez la fréquence des acides aminés alanine (A), arginine (R), tryptophane (W) et glycine (G) dans cette séquence.

a=0
r=0
w=0
g=0

for i in acide:
    if i=="A":a=a+1
    elif i=="R":r=r+1
    elif i=="W":w=w+1
    elif i=="G":g=g+1
    else : break

print(f"la fréquence d'alanine (A)est {a/len(acide)*100:.2f}%")
print(f"la fréquence d'arginine (R) est {r/len(acide)*100:.2f}%")
print(f"la fréquence de tryptophane (W) est {w/len(acide)*100:.2f}%")
print(f"la fréquence de glycine (G) est {g/len(acide)*100:.2f}%")

print(f"le total des fréquences est {(a+r+w+g)/len(acide)*100}%")

#6.7.5 Notes et mention d’un étudiant
note=[14, 9, 13, 15 , 12]
print(f"la note minimale est {min(note)}")
print(f"la note maximale est {max(note)}")
print(f"la moyenne des notes est {sum(note)/len(note):.2f}")

moy=sum(note)/len(note)

if 10<=moy<12: print("la mention est passable")
elif 12<=moy<14: print("la  mention est assez bien")
elif moy>14: print("la mention est bien")


#6.7.6 Nombres pairs
#Construisez une boucle qui parcourt les nombres de 0 à 20 et qui affiche les nombres 
#pairs inférieurs ou égaux à 10 d’une part, et les nombres impairs strictement 
#supérieurs à 10 d’autre part
#Pour cet exercice, vous pourrez utiliser l’opérateur modulo % qui renvoie le reste de la 
#division entière entre deux nombres




for i in range(20):
    if (i%2==0) and (i<=10): print(i)
    if (i%2==1) and (i>10): print(i)

#0
#2
#4
#6
#8
#10
#11
#13
#15
#17
#19

#6.7.7 Conjecture de Syracuse (exercice +++)
#La conjecture de Syracuse est une conjecture mathématique qui reste improuvée à ce jour 
#et qui est définie de la manière suivante.
#Soit un entier positif n. Si n est pair, alors le diviser par 2. Si il est impair, 
#alors le multiplier par 3 et lui ajouter 1. 
#En répétant cette procédure, la suite de nombres atteint la valeur 1 puis se prolonge 
#indéfiniment par une suite de trois valeurs triviales appelée cycle trivial.
#Jusqu’à présent, la conjecture de Syracuse, selon laquelle depuis n’importe quel entier 
#positif la suite de Syracuse atteint 1, n’a pas été mise en défaut.
#Par exemple, les premiers éléments de la suite de Syracuse si on prend comme point de 
#départ 10 sont : 10, 5, 16, 8, 4, 2,1...

#Créez un script qui, partant d’un entier positif n (par exemple 10 ou 20), 
#crée une liste des nombres de la suite de Syracuse.
#Avec différents points de départ (c’est-à-dire avec différentes valeurs de n), 
#la conjecture de Syracuse est-elle toujours vérifiée ?
#Quels sont les nombres qui constituent le cycle trivial ?


start=51
syra=[start]
n=30

for i in range(n):
    if syra[i]%2==0:syra=syra+[syra[i]/2]
    else:  syra=syra+[syra[i]*3+1]

for i in range(n) : print(f"{syra[i]:.00f}")

#les derniers termes sont:
#4
#2
#1
#4
#2
#1
#4
#2

#6.7.8 Attribution de la structure secondaire des acides aminés d’une protéine (exercice +++)
ma_liste= [[48.6 , 53.4] ,[ -124.9 , 156.7] ,[ -66.2 , -30.8] , \
[-58.8 , -43.1] ,[ -73.9 , -40.6] ,[ -53.7 , -37.5] , \
[-80.6 , -26.0] ,[ -68.5 , 135.0] ,[ -64.9 , -23.5] , \
[-66.9 , -45.5] ,[ -69.6 , -41.0] ,[ -62.7 , -37.5] , \
[-68.2 , -38.3] ,[ -61.2 , -49.1] ,[ -59.7 , -41.1]]

len(ma_liste)
#15
ma_liste[0][0]
#48.6
ma_liste[0]
#[48.6, 53.4]
delta=30
val1=-57
val2=-47
k=0

for i in range(len(ma_liste)):
        if (val1-delta<ma_liste[i][0]<val1+delta) and (val2-delta<ma_liste[i][1]<val2+delta):
            print(f" {ma_liste[i]} est en hélice")
            k=k+1
        else: print(f" {ma_liste[i]} n'est en hélice")  
                  
print(f"sur 15 acides aminés, {k} sont en hélice ")


#6.7.9 Détermination des nombres premiers inférieurs à 100 (exercice +++)

#Méthode 1 (peu optimale mais assez intuitive)
#Pour chaque nombre de 2 à 100, calculez le reste de la division entière (avec l’opérateur 
#modulo %) depuis 1 jusqu’à lui-même. Si c’est un nombre premier, il aura exactement deux
# nombres pour lesquels le reste de la division entière est égal à 0 (1 et lui-même). 
#Si ce n’est pas un nombre premier, il aura plus de deux nombres pour lesquels le reste 
#de la division entière est égal à 0.

n=100
premier=[]

for i in range(2,n):
    compteur=0
    for j in range(1,i+1): 
        if (i%j==0) : compteur=compteur+1
    if (compteur==2) : premier=premier+[i]
print(premier)
#résultat:
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

#Méthode 2 (plus optimale et plus rapide, mais un peu plus compliquée)
#Parcourez tous les nombres de 2 à 100 et vérifiez si ceux-ci sont composés, 
#c’est-à-dire qu’ils sont le produit de deux nombres premiers.
#Pratiquement, cela consiste à vérifier que le reste de la division entière 
#(opérateur modulo %) entre le nombre considéré et chaque nombre premier déterminé 
#jusqu’à maintenant est nul. Le cas échéant, ce nombre n’est pas
#premier. Attention, pour cette méthode, il faudra initialiser la liste de nombres 
#premiers avec le premier nombre premier (donc 2 !).

#a finir
n=100
premier2=[1]

for i in range(2,n):
    compteur=0
    for j in premier2 :
        if (i%j==0) : compteur=compteur+1
    if (compteur==1) : premier2=premier2+[i]
print(premier2)
#Erésultat
#[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]             
 
#6.7.10 Recherche d’un nombre par dichotomie (exercice +++)




#Pour vous guider, voici ce que donnerait le programme avec la conversation précédente :
print(" Pensez à un nombre entre 1 et 100")

print("Est - ce votre nombre est plus grand , plus petit ou égal à 50 ?")

#a revoir plus tard (ne marche pas)
n=100
nb=100/2
nb2=0
intervalle=[1,n]
print(f"Est-ce votre nombre est plus grand, plus petit ou égal à {n/2} [+/-/=] ?")
signe=input()

while (signe!="="):
    if signe=="+": nb=nb+int((n-nb)/2) \
        and print(f"Est-ce votre nombre est plus grand, plus petit ou égal à {nb} [+/-/=] ?")     #intervalle=[int(n/2),n]
    elif signe=="-": nb=nb-int((n-nb)/2) \
        and print (f"Est-ce votre nombre est plus grand, plus petit ou égal à {nb} [+/-/=] ?")    #intervalle=[1,int(n/2)]
   
print(f"Est-ce votre nombre est plus grand, plus petit ou égal à {n/2} [+/-/=] ?")   
 ##################################

#7.7 Exercices

#7.7.1 Moyenne des notes

path2="C:/Users/Francis/R_new/Python Scripts/Cours Paris 7/data/"

with open (path2+"notes.txt","r") as filin :
    lignes = filin.readlines()
    lignes

notes=[]
for ligne in lignes :
    notes=notes+[ligne]

print(notes)

notes2=[]
for note in notes:
    note=float(note)
    notes2=notes2+[note]
    
notes2


moy=sum(notes2)/len(notes2)
print(f"la moyenne vaut {moy:.2f}")




                
                  