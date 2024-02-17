# -*- coding: utf-8 -*-
"""
Escribe un programa que dado un número entero n indique todos los números primos de 2 a n

@author: erick
"""

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

while num2 > 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp
    
print(num1)