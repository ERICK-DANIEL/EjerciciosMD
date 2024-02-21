# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:19:25 2024

@author: erick
"""

n = int(input("Ingrese el numero de filas a generar: "))

Triangulo = [[1]]
for i in range(1, n):
    filaTriangulo = [1]
    for j in range(1, i):
        filaTriangulo.append(Triangulo[i-1][j-1] + Triangulo[i-1][j])
    filaTriangulo.append(1)
    Triangulo.append(filaTriangulo)

for filaTriangulo in Triangulo:
    print(filaTriangulo)