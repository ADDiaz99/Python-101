# Tuplas
# https://www.w3schools.com/python/python_tuples.asp

'''
Las tuplas son inmutables, es decir que no podemos
realizar cambios sobre ellas.
En la tupla solo podemos realizar la declaración.
'''

numbers = (1, 2, 3, 4, 5)

print(numbers)
print(type(numbers))
print("0 =>", numbers[0])
print("-1 =>", numbers[-1])

strings = ('Sara', 'Nico', 'Freddy', 'Nico')
print(strings)
print(type(strings))

# Métodos
# Buscar elementos dentro de la tupla
print(strings.index("Sara"))

# Contar cuantas veces está un elemento dentro de la tupla
print(strings.count("Nico"))

# Pasar una tupla a lista
my_list = list(strings)
# Vemos que al imprimir se muestra entre [] correspondientes a listas
print(my_list)
print(type(my_list))

# Modificar lista
my_list[1] = "Juli"
print(my_list)

# Pasar una lista a una tupla
my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))