# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:32:55 2024

Programa que dice si dos numeros son amigos
@author: erick
"""

numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa un numero: "))

suma1 = 0
for i in range(1, numero1):
    if numero1 % i == 0: 
        suma1 = suma1 + i
        
suma2 = 0
for i in range(1, numero2):
    if numero2 % i == 0: 
        suma2 = suma2 + i
        
if suma1 == numero2 and suma2 == numero1:
    print("Los numeros son amigos")
else:
    print("Los numeros No son amigos")