n = int(input("Ingrese el numero de filas a generar: "))

Triangulo = [[1]]
for i in range(1, n):
    filaTriangulo = [1]
    for j in range(1, i):
        filaTriangulo.append(Triangulo[i-1][j-1] + Triangulo[i-1][j])
    filaTriangulo.append(1)
    Triangulo.append(filaTriangulo)

for filaTriangulo in Triangulo:
    text = str(filaTriangulo)
    x = text.center(n * 10)
    print(x)