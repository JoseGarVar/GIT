matriz = []

filas = int(raw_input("Cuantas Filas: "))
columnas = int(raw_input("Cuantas Columnas: "))

for i in range(filas):
    matriz.append([0] * columnas)

for f in range(filas):
    for c in range(columnas):
        matriz[f][c] = int(raw_input("Elemento %d,%d: " %(f,c)))
        
print matriz