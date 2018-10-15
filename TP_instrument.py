#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 13:39:09 2018

@author: 3874345
"""

import vxi11
import matplotlib.pyplot as plt
import numpy as np

#oscillo = vxi11.Instrument('134.157.91.150')

#identification = oscillo.inst.ask('*IDN?')

#type(identification)

class TextronixMSO3014(object):
    def __init__(self,adresseIP):
        self.inst = vxi11.Instrument(adresseIP)
        print(self.get_idn())
    
    def get_idn(self):
        return self.inst.ask('*IDN?')
    
    def lock(self):
        try:
            self.inst.lock()
            self.locked_by_me = True
        except:
            if self.locked_by_me:
                print('You have already locked the instrument')
            else:
                print('Someone has locked the Instrument')
    
    def unlock(self):
        try:
            self.inst.unlock()
            self.locked_by_me = False
        except:
            if self.locked_by_me:
                print('Unlock does not work')
            else:
                print('Cannot Unlock Instrument. Instrument was locked by another student')
                
    #Fonctions perso
    
    def get_vert_scale(self,channel):
        #value = self.inst.ask('CH'+channel+':SCAle?')
        return self.inst.ask('CH'+str(channel)+':SCAle?')
    
    def set_vert_scale(self,channel,value):
        self.inst.write('CH'+str(channel)+':SCAle '+str(value))
        
    def get_horiz_scale(self):
        return self.inst.ask('HORizontal:SCAle?')
    
    def set_horiz_scale(self,value):
        self.inst.write('HORizontal:SCAle '+str(value))
    
    def ask_for_value(self, ma_chaine):
        return float(self.inst.ask(ma_chaine))
    
    def reset(self):
        self.inst.write('*RST')
    
    def get_curve(self,channel):
        self.inst.write('DATa:ENCdg ASCII')
        self.inst.write('DATA:SOURCE CH'+str(channel))
        return self.inst.ask('CURve?')
    
    def get_vert_position(self,channel):
        self.inst.write('DATa:ENCdg ASCII')
        verticalPosition = self.inst.ask('WFMOutpre:YOFf?')
        return verticalPosition
    
    def get_output_bit(self,channel):
        self.inst.write('DATa:ENCdg ASCII')
        return self.inst.ask('WFMOutpre:BIT_Nr?')
        
    
try:
    oscillo = TextronixMSO3014('134.157.91.150');
    oscillo.lock();

    #oscillo.get_idn()
    
    oscillo.set_vert_scale(1,0.3);
    oscillo.set_horiz_scale(10e-6);
    #oscillo.reset()
    vertScale = oscillo.get_vert_scale(1);
    horizScale = oscillo.get_horiz_scale();
    
    vertPosition = oscillo.get_vert_position(1);
    outputBit = oscillo.get_output_bit(1);
    
    data = oscillo.get_curve(1);
    curve = data.split(',')
    
    oscillo.unlock();

except:
    oscillo.unlock();

x1 = -len(curve)/2.*horizScale;
x2 = -x1;
xlin = np.linspace(x1,x2,num=len(curve))
plt.plot(curve) 