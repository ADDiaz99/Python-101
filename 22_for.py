''''
for element in range(1, 21):
    print(element)
'''

my_list = [23, 45, 67, 89, 43]
for i in my_list:
    print(i)

my_tuple = ('nico', 'juli', 'santi')
for i in my_tuple:
    print(i)

#EJERCICIO
'''
En este desafío, se te proporcionará una lista de números llamada my_list. 
Tu tarea es recorrer esta lista y utilizar un ciclo para seleccionar solo los números positivos. 
Luego, debes agregar estos números a una nueva lista llamada new_list. 
Al final del ciclo, debes imprimir los valores contenidos en new_list utilizando la función print.

Por ejemplo, si la lista es [1, -1, 2, -2, 3, -3, 4, -4], después de realizar las operaciones descritas,
la lista new_list debería contener solo los números positivos, es decir, [1, 2, 3, 4].

'''
#SOLUCION:

my_list = [1, -1, 2, -2, 3, -3, 4, -4]
new_list = []

for number in my_list: #Por cada numero en mi lista...
  if number > 0: #Si el numero es mayor que 0...
    new_list.append(number) #Agrega el numero a la nueva lista
    
print(new_list)