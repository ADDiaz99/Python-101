print("Este es el archivo 02_vars")

precio = input('Masita, dime cual es el precio del objeto?')
print(precio)

cantidad = input("y Cuantos objetos vendiste?")
print(cantidad)

precio = int(precio)
cantidad = int(cantidad)

resultado = precio * cantidad
print("Tus ganancias fueron de", resultado)
