#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 13:35:47 2018

@author: 3874345
"""

import numpy as np
from matplotlib.pyplot import *

class Dioptre():
    # R>0: dioptre convexe
    # R<0: dioptre concave
    
    #diametre = 25.4
    def __init__(self, z0, R, n_1, n_2, diametre=None):
        self.z0 = z0
        self.R = float(R)
        if diametre is not None:
            self.diametre = diametre
            self.n_1 = n_1
            self.n_2 = n_2
            self.z_center = self.z0
            self.z_center[2] += R
            
    def __repr__(self):
        return("Centre: "+str(self.z_center)+"\nRayon: "+str(self.R))
    
    def equation(self,y):
        y2 = y**2; R2 = (self.R)**2
        x2 = np.zeros(len(y))
        x2 = [R2-i for i in y2 if R2 >= i]
        return(np.sign(self.R)*(self.z_center[0] -np.sqrt(x2)))

    def plot(self,start=-10,stop=10):
        y = np.linspace(start,stop,100)
        x = self.equation(y)
        plot(x,y)
        axis('equal')

    def intersec(self,rayon):
        center = self.z_center; R = self.R
        p1 = rayon.p0; k1 = rayon.k

        # Calcul du point d'intersection
        a = np.sum(k1**2)
        b = 2*np.dot(k1,p1-center)
        c = np.sum((p1-center)**2)-R**2
        
        discriminant = b**2-4*a*c
        if discriminant<0:
            return("Pas de solution pour l'intersection")
        
        t = (-b-np.sign(R)*np.sqrt(discriminant))/(2*a)
        
        p2 = p1 + t*k1
        return(p2)
    
    def traversee(self,rayon):
        center = self.z_center; R = self.R

        p1 = rayon.p0; k1 = rayon.k
        p2 = self.intersec(rayon)
        
         # Calcul du vecteur normal à la surface en ce point
        n = [p2[0]-center[0], p2[1]-center[1], p2[2]-center[2]]
        norme = np.linalg.norm(n)
        n = [i/norme for i in n]
        
        # Calcul du vecteur tangent à la surface en ce point
        kt = [k1[0] - np.dot(k1,n)*n[0], k1[1] - np.dot(k1,n)*n[1], k1[2] - np.dot(k1,n)*n[2]]
        
        # Calcul du vecteur refracté
        alphaCarre = np.power(self.n_2, 2)-np.power(np.linalg.norm(kt), 2)
        alpha = np.sign(R)*(np.sqrt(np.abs(alphaCarre)))
        
        k2 = [kt[0] + alpha*n[0], kt[1] + alpha*n[1], kt[2] + alpha*n[2]]
        
        rayon2 = Rayon(p2,k2)
        
        return(rayon2)
        
class Rayon():
    def __init__(self,p0,k):
        self.p0 = p0
        norme = np.linalg.norm(k)
        self.k = np.array(k)/norme
    
    def __repr__(self):
        return("Point initial: "+str(self.p0)+"\nVecteur propagation (normalisé): "+str(self.k))
    
R = 6
dioptre1 = Dioptre(np.array([0,0,0]),R,1,1.5,10)
rayon = Rayon(np.array([0,0,0]),np.array([1,1,0]))
rayon2 = dioptre1.traversee(rayon1)

#dioptre1.plot(-R,R)
#p1x = rayon1.p0[0]; p1y = rayon1.p0[1]
#p2x = rayon2.p0[0]; p2y = rayon2.p0[1]
#plot([p1x, p1y] , [p2x, p2y])

z0=np.array([0,0,0])
z_center = z0
z_center[2] += R
center=z_center

class Faisceau(list):
    def plot(self):
        nbRayons = len(self)
        if nbRayons >= 2:
            x = np.zeros(nbRayons)
            y = np.zeros(nbRayons)
            z = np.zeros(nbRayons)
            for i in range(nbRayons):
                rayon = self[i]; p = rayon.p0
                x[i] = p[0]; y[i] = p[1]; z[i] = p[2]
            for i in range(nbRayons-1):
                plot([x[i], x[i+1]], [y[i], y[i+1]])
    
class SystemeOptique(list):
    def calcul_faisceau(self,r0):
        faisceau = Faisceau()
        faisceau.append(r0)
        for dioptre in self:
            faisceau.append(dioptre.traversee(faisceau[-1]))
        return faisceau
    def plot(self):
        for dioptre in self:
            dioptre.plot()

        
