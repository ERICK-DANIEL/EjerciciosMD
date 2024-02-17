# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 18:46:36 2024

@author: erick
"""

num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

while num2 > 0:
    num1, num2 = num2, num1 % num2
    
print(num1)