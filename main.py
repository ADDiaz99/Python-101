#Este es un juego de piedra papel o tijera en paito xd

import random

options = ('piedra', 'papel', 'tijera')

user_wins = 0
computer_wins = 0
rounds = 1

while True:

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('Puntaje del Jugador: ', user_wins)
    print('Puntaje de la Computadora: ', computer_wins)

    user_option = input("Bienvenido, elige: Piedra, papel o tijera?")
    user_option = user_option.lower()

    
    if user_option not in options:
        print('Esa opcion no es valida')
        continue
    
    rounds +=1           	
    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    if user_option == computer_option:
        print('Empate!')

    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra le gana a tijera')
            print('El Usuario ganó!!!')
            user_wins += 1
        if computer_option == 'papel':
            print('Papel le gana a tijera')
            print('La computadora gana!')
            computer_wins +=1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel le gana a tijera')
            print('El Usuario gana!!')
            user_wins += 1
        if computer_option == 'tijera':
            print('tijera le gana a papel!')
            print('La computadora gana!')
            computer_wins +=1
    elif user_option == 'tijera':
        if computer_option == 'papel':  
            print('Tijera le gana al papel')
            print('El usuario gana!')
            user_wins += 1
        if computer_option == 'piedra':
            print('Piedra le gana a papel')
            print('La computadora gana!')
            computer_wins +=1
    
    if computer_wins == 2:
        print('La computadora gana el juego!!!!')
        break
    if user_wins == 2:
        print('El usuario gana el juego!!!!')
        break
    
    
        