# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
# -*- coding: utf-8 -*-
import pulp as pulp

tab =[]
Objets = []
valeur = []
poids = []
volume = []

mon_fichier = open("c:\jeuEssai3.txt","r")
f=mon_fichier.readlines()
nbLignes = len(f)
NbObjet = int(f[0])
PoidsMax = float(f[nbLignes-2])
VolumeMax = float(f[nbLignes-1])

i = 1
while i <= NbObjet:
    ligne=f[i].split()
    
    for j in range(len(ligne)):
        c=ligne[j]
        d=tab.append(c)
    i += 1
print(tab)
print("")

ValeurMoyenne=0
PoidsMoyen=0
VolumeMoyen=0


"""
jeu Essai 1a
"""
o=1
index=0
while o<= NbObjet:
    ValeurMoyenne+=int(tab[index])
    PoidsMoyen+=int(tab[index+1])
    VolumeMoyen+=int(tab[index+2])
    valeur.append(tab[index])
    poids.append(tab[index+1])
    volume.append(tab[index+2])
    
    o+=1
    index+=3 
    """ pour le jeuEssai1b"""

        
ValeurMoyenne /= NbObjet
PoidsMoyen /= NbObjet    
VolumeMoyen /= NbObjet

print("")
print("tableau des valeurs")
print("")
print(valeur)
print("")
print("tableau des poids")
print("")
print(poids)
print("")
print("tableu des volumes")
print("")
print(volume)
print("")
print("La valeur moyenne des objets est ",ValeurMoyenne)
print("Le poid moyen des objets est ",PoidsMoyen)
print("Le volume moyen des objets est ",VolumeMoyen)
print("")

"""
jeuEssai2 et jeuEssai3
"""

my_lp_problem = pulp.LpProblem("My LP Problem",pulp.LpMaximize)

"""
Variables de décision
"""
x = pulp.LpVariable.dicts("x", [i for i in range(len(valeur))], cat = "Binary")

"""
Contraintes
"""

my_lp_problem += pulp.lpSum([int(valeur[i])*x[i] for i in range(len(valeur))])
my_lp_problem += pulp.lpSum(int(poids[i])* x[i] for i in range(len(valeur)))<=PoidsMax
my_lp_problem += pulp.lpSum(int(volume[i])* x[i] for i in range(len(valeur)))<=VolumeMax

"""
Resolution problème
"""

print(my_lp_problem)
my_lp_problem.solve()
print(pulp.LpStatus[my_lp_problem.status])
for variable in my_lp_problem.variables():
    print(variable.name, variable.varValue)

"""
Affichage de la solution
"""

print("La valeur de l'objectif est :", pulp.value(my_lp_problem.objective))
