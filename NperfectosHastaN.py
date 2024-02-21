# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:17:09 2024

Programa para ver que numeros son perfectos desde un numero dado
@author: erick
"""

numero = int(input("Ingresa un numero: "))

print("Numeros perfectos: ")

for n in range(1, numero):
    suma = 0
    for i in range(1, n):
        if n % i == 0: 
            suma = suma + i
            
    if suma == n:
        print(n)



