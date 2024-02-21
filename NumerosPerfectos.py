# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:29:23 2024

Programa para saber si un numero es perfecto
@author: erick
"""

n = int(input("Ingresa un numero: "))

suma = 0

for i in range(1, n):
    if n % i == 0: 
        suma = suma + i

if suma == n:
    print("El numero", n, "es perfecto")
else:
    print("El numero", n, "NO es perfecto")

    
