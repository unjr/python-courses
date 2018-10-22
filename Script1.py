#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 13:32:32 2018

@author: NAJAR Ulysse
"""

# Question 1
ma_liste = list(range(20,300,7));


# Question 2
ma_nouvelle_liste = [i for i in ma_liste if i%5==0];


# Question 3
print(ma_liste)


# Question 4 (dans cette question, la variable ma_chaine est une liste de chaines de caracteres)
ma_chaine = [str(i) for i in ma_liste];


# Question 5 (dans cette question, la variable ma_chaine est une chaine de caracteres)
ma_chaine = '128967023098';
ma_nouvelle_chaine = ma_chaine.split('0');


# Question 6
from math import *
ma_liste_finale = list(map(lambda x:cos(x), ma_liste));

# Question 7
annuaire = {'Jacqmin':'0687459830', 'Cladé':'0678236475'}

# Question 8
annuaire['Maitre'] = '0690783654'

# Question 9
annuaire.popitem()

# Question 10
def save_to_file(dico):
    f = open('/users/etu/3874345/Téléchargements/dico.txt', 'w')
    listeChaines = []
    for clef,valeur in dico.items():
        listeChaines.append('{0}, {1}'.format(clef,valeur))
    f.write('\n'.join(listeChaines))
    f.close()

save_to_file(annuaire)

# Question 11
def load_from_file(filename):
    dico = dict()
    f = open('/users/etu/3874345/Téléchargements/'+filename+'.txt', 'r')
    chaine = f.read()
    f.close()
    lignes = chaine.split('\n')
    for entree in lignes:
        entree = entree.split(',');
        dico[entree[0]]=entree[1]
    return dico

annuaireBis=load_from_file('dico')

# Question 12
import os
def delete_file(filename):
    os.remove('/users/etu/3874345/Téléchargements/'+filename+'.txt')
    