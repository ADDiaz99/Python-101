print('Bienvenido..! en este programa te dire si un número es par o impar.')
print()

num = int(input('Escribe un número un numero: '))

if num % 2 == 0:
  print(f'{num} es número par')
else:
  print(f'{num} es número impar')