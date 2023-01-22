# CRUD Means: Create, Read, Update and Delete

numbers = [1, 2, 3, 4, 5] # Create
print(numbers[1]) # Read
numbers[-1] = 10 # Update
print(numbers)

# Update
# Agregar elementos al final de la lista
numbers.append(700)
print(numbers)
# Agregar elementos en una posicion definida de la lista
numbers.insert(0, 'hola')
print(numbers)
numbers.insert(3, 'change')
print(numbers)

# Unir listas
tasks = ["to do 1", "to do 2", "to do 3"]
new_list = numbers + tasks
print(new_list)

# Consultar la posicion de un valor específico y actualizarlo
index = new_list.index("to do 2")
print(index)
new_list[index] = "to do changed"
print(new_list)

# Delete
new_list.remove("to do 1")
print(new_list)

# Eliminar el último elemento de la lista
new_list.pop()
print(new_list)

# Eliminar una posición específica de la lista
new_list.pop(0)
print(new_list)

# Voltear todo el array
new_list.reverse()
print(new_list)

# Ordenar
numbers_a = [1, 4, 6, 3]
print(numbers_a)

numbers_a.sort()
print(numbers_a)

strings = ["re", "ab", "ed"]
print(strings)
strings.sort()
print(strings)

'''
Cuando se tiene un array con diferentes tipos de datos mezclados
el método sort no es funcional

new_list.sort()
print(new_list)

Comandos utiles:
append(): Añade un ítem al final de la lista.
clear(): Vacía todos los ítems de una lista.
extend(): Une una lista a otra.
count(): Cuenta el número de veces que aparece un ítem.
index(): Devuelve el índice en el que aparece un ítem (error si no aparece).
insert(): Agrega un ítem a la lista en un índice específico.
pop(): Extrae un ítem de la lista y lo borra.
remove(): Borra el primer ítem de la lista cuyo valor concuerde con el que indicamos.
reverse(): Le da la vuelta a la lista actual.
sort(): Ordena automáticamente los ítems de una lista por su valor de menor a mayor.
'''

# PLAYGROUND: 
#En este desafío, se te proporcionará una lista de letras llamada letters. Tu reto es realizar las siguientes operaciones en orden:

#Agregar la letra G al final de la lista.
#Reemplazar la letra en la posición 0 con la letra Z.
#Eliminar la letra C de la lista.
#Imprimir la lista resultante al revés.
# La lista es: letters = ['A', 'B', 'C', 'D', 'E', 'F']

#SOLUCION:

letters = ['A', 'B', 'C', 'D', 'E', 'F']

letters.append('G')
letters[0] = 'Z'
letters.remove('C')
letters.reverse()
print(letters)

