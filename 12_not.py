try:
    age = int(input('¿Edad? '))
    puede_votar = not age < 18
    print('¿Puede votar?: ', puede_votar)
except:
    print('Escribe tu edad en número entero')