#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:27:44 2018

@author: NAJAR Ulysse
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import airy
from scipy.integrate import odeint
from scipy.signal import argrelextrema
from scipy.optimize import curve_fit

# Question 1
A = np.arange(0,20,1).reshape(4,5);

# Question 2
A[A%2 == 1] = 0

# Question 3 
elementsNonNuls = A[A != 0]; # on stocke les elements non nuls de A dans une liste

# Question 4
B = np.diag([i**2 for i in range(10)]);

# Question 5
np.save('/users/etu/3874345/Téléchargements/fichierBinaire',B)

# Question 6
# Fonctions d'Airy
x = np.linspace(-15,1,200);
ai, aip, bi, bip = airy(x);

plt.figure(1)
Ai = plt.plot(x, ai+1.5, 'b-.')
Bi = plt.plot(x, bi, 'r-')

l0 = plt.hlines(0,-15,1)
l1 = plt.hlines(1.5,-15,1)

plt.xlim(-16,2)
plt.xlabel('x')
plt.ylabel('y')
plt.yticks([])
plt.title("Fonctions d'Airy Ai et Bi")


# Question 7
a = 0.2; b=1; t = np.linspace(0, 40, 500);
y0 = [0,1];
def derivee(y,t,a,b): # On définit la dérivée de y(t)
    theta,omega = y;
    dydt = [omega,-a*omega-b*theta];
    return dydt
sol = odeint(derivee,y0,t,args=(a,b))
y = sol[:, 0];

plt.figure(2)
plt.plot(t, y, 'b', label = 'y(t)')
plt.grid()
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title("Oscillateur harmonique amorti")

# Question 8
# Commencer par trouver les maxima locaux
yLocalMaxima = y[argrelextrema(y, np.greater)[0]]
xLocalMaxima = t[argrelextrema(y, np.greater)[0]]

plt.plot(xLocalMaxima,yLocalMaxima,'rx')
# Puis fitter les données avec une exponentielle
def exponential_func(x, a, b, c): # definition de la fonction exp avec les parametres à faire varier
    return a*np.exp(-b*x)+c

popt, pcov = curve_fit(exponential_func, xLocalMaxima, yLocalMaxima, p0=(1, 1e-6, 1))
xFit = t;
yFit = exponential_func(xFit, *popt)
plt.plot(xFit,yFit,'r-')

# On retrouve les coefficients de l'exponentielle:

a = popt[0]; b = popt[1]; c = popt[2]
print('{0} exp(-{1} t) + {2}'.format(a,b,c))

# On peut verifier que cela est cohérent avec les valeurs choisies en question 7
