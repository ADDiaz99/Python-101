# Indexing : Significa que los textos tienen un indicador en el cual yo puedo ingresar a nivel de posiciones. 

text = "Ella sabe Python"
print(text[0])
print(text[1])
# En la mayoria de lenguajes,la primer posicion es 0. 

print(text[999]) #Este por ejemplo no la encuentra

# Como saber cual es el caracter final 
size = len(text)
print('size => ',size)
print(text[size - 1])

# 0 le damos el texto y le restamos 1
print(text[-1])

# slicing : Basado en las posiciones de los caracteres , podemos sacar ciertas partes del texto. 

# Obtener el texto de ese rango 
print(text[0:5])
print(text[10:16])
print(text[:10])
print(text[5:-1])

#Cuando no se pone nada , quiere decir que ira hasta el final del texto 
print(text[5:])
print(text[:])

# Saltos , el tercer valor es cuanto salto de letra en letra 
print(text[10:16:1])
print(text[10:16:2])
print(text[::2])