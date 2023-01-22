#Este es un juego de piedra papel o tijera en paiton

user_option = input("Bienvenido, elige: Piedra, papel o tijera?")
user_option = user_option.lower()
computer_option = 'papel'

if user_option == computer_option:
    print('Empate!')

elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('piedra le gana a tijera')
        print('El Usuario ganó!!!')
    if computer_option == 'papel':
        print('Papel le gana a tijera')
        print('La computadora gana!')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('Papel le gana a tijera')
        print('El Usuario gana!!')
    if computer_option == 'tijera':
        print('tijera le gana a papel!')
        print('La computadora gana!')
elif user_option == 'tijera':
    if computer_option == 'papel':  
        print('Tijera le gana al papel')
        print('El usuario gana!')
    if computer_option == 'piedra':
        print('Piedra le gana a papel')
        print('La computadora gana!')
        