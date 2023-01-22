name = "Andres"
last_name = "Diaz Rincon"

print(name)
print(last_name)

full_name = name + ' ' + last_name
print(full_name)

quote = "I'm Andres"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

#sin format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('version concat:', template)

#con format
template = "Hola, mi nombre es {} y mi apellido es {}" .format(name, last_name)
print('version format:', template)

#con f
template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('version f:', template)

#ejemplo complejo
edad = input("Que edad tienes?")
vivienda = input ("Donde vives?")
hobby = input("Cual es tu hobby favorito?")

ejemplotemplate = f"Hola, mi nombre es {name} y mi apellido es {last_name}, Vivo en {vivienda}, tengo {edad} y mi pasatiempo favorito es {hobby}"
print(ejemplotemplate) 