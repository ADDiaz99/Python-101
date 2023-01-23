# Ciclos anidados

matriz = [
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
]

# Imprime la primera fila de la matriz
print(matriz[0])

# Imprime el elemento 2 de la primera fila
print(matriz[0][1])

'''
Recorremos las filas de la matriz y por cada fila recorremos cada una de las columnas
'''
for row in matriz:
  print(row)
  for column in row:
    print(column)