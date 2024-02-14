# -*- coding: utf-8 -*-
"""
Escribe un programa que solicite si un numero es primo
"""

numero = int(input("Ingresa un numero: "))

primo = True

for i in range (2, numero // 2 + 1):
    if (numero % i == 0):
        primo = False
        break

if(primo == False):
    print("Numero no es primo")
else: 
    print("numero es primo")
    