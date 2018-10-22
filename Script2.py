#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 14:22:42 2018

@author: NAJAR Ulysse
"""
import os

class Bibliotheque(list):
    def __init__(self):
        self.current_index = 0;
    
    def ajout(self,livre):
        self.append(livre); # chaque livre est stocké dans la classe Bibliotheque, sous forme de liste
        self.current_index += 1;
        livre.index = self.current_index; # l'indice n'est pas stocke dans le dictionnaire et donc ne s'imprime pas dans le fichier !
        livre.save_to_file();
    
    def find_index(self,propriete,valeur):
        for livre in self:
            if livre[propriete] == valeur:
                return livre.index
            else:
                return('Aucun livre ne correspond.')
    
    def suppression(self,entier):
        for i,livre in enumerate(self):
            if livre.index == entier:
                del self[i]
                livre.delete_file()
                return('Livre supprimé.')
        return('Aucun livre ne correspond.')

    def pret(self,index):
        for i,livre in enumerate(self):
            if livre.index == index:
                livre.emprunt = True;
                return('Emprunt effectué.')
        return('Aucun livre ne correspond.')
    
    def retour(self,index):
        for i,livre in enumerate(self):
            if livre.index == index:
                livre.emprunt = False;
                return('Retour effectué.')
        return('Aucun livre ne correspond.')
    
    def __repr__(self):
        listeLivres = [];
        for livre in self:
            listeLivres.append('Livre n°{0}: {1} de {2}, publié en {3} par {4}'.format(livre.index,livre['Titre'],livre['Auteur'],livre['Annee de publication'],livre['Editeur']));
        retour = '\n'.join(listeLivres)
        return(retour)

    
class Livre(dict):
    def __init__(self,titre='',auteur='',annee_publication='',editeur='',emprunt=False):
        self['Titre'] = titre;
        self['Auteur'] = auteur;
        self['Annee de publication'] = annee_publication;
        self['Editeur'] = editeur;
        self.emprunt = emprunt;
    
    def save_to_file(self):
        f = open('/users/etu/3874345/Téléchargements/'+self['Titre']+'.txt', 'w')
        listeChaines = []
        for clef,valeur in self.items():
            listeChaines.append('{0} : {1}'.format(clef,valeur))
        f.write('\n'.join(listeChaines))
        f.close()
    
    def load_from_file(self,filename):
        dico = dict()
        f = open('/users/etu/3874345/Téléchargements/'+filename+'.txt', 'r')
        chaine = f.read()
        f.close()
        lignes = chaine.split('\n')
        for entree in lignes:
            entree = entree.split(',');
            dico[entree[0]]=entree[1]
        return dico
    
    def delete_file(self):
        os.remove('/users/etu/3874345/Téléchargements/'+self['Titre']+'.txt')   
    
    def __repr__(self):
        return("Titre: {0}\nEcrit par {1}\nPublié en {2} par {3}".format(self['Titre'],self['Auteur'],self['Annee de publication'],self['Editeur']))



# Exemples d'utilisation

l1 = Livre(titre='Le maitre et la marguerite',auteur='Mikhail Boulgakov',annee_publication='1939',editeur='Laffont');
l2 = Livre(titre='Cent ans de solitude',auteur='Gabriel Garcia Marquez',annee_publication='1967',editeur='Seuil');
l3 = Livre(titre='La caverne des idees',auteur='Jose Carlos Somoza',annee_publication='2003',editeur='Actes Sud');

b = Bibliotheque();
b.ajout(l1)
b.ajout(l2)
b.ajout(l3)

b.find_index('Titre','Le maitre et la marguerite')

print(b)
