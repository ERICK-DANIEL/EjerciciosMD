# -*- coding: utf-8 -*-
"""
Escribe un programa que dado un número entero n indique todos los números primos de 2 a n

@author: erick
"""
def primos(Pnumero):
    for numero in range(2, Pnumero + 1):
        
        primo = True
        
        for i in range(2, numero // 2 + 1):
            if numero % i == 0:
                primo = False
                break
            
        if primo:
            print(numero)
            
Pnumero = int(input("Ingresa un numero: "))

primos(Pnumero)