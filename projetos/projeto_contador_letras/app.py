var_choice = input('Deseja iniciar o contador de letras? ')

if var_choice == 'Sim':
    var_char = input('Insira uma palavra: ')
    var_char = var_char.replace(" ", "")

    print(f'A palavra {var_char} tem {len(var_char)} letras.')
elif var_choice == 'Não':
    print('Ok, Saindo!')
else:
    print('Error001: valor invalido!')
