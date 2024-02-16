# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 12:26:35 2024

@author: zS23021810
"""

Numero1 = int(input("Ingresa el primer numero: "))
resto = int(input("Ingresa el segundo numero: "))

while (Numero1 != 0 and resto != 0):
    resto = Numero1 % resto
    Numero1 = resto
    
    print(resto)

    
    