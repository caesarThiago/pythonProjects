var_choice = input('Deseja identificar se o número é par ou ímpar? ')

if var_choice == 'Sim':
    var_num = int(input('Digite um número inteiro: '))

    if var_num % 2 == 0:
        print(f'O {var_num} é par!')
    else:
        print(f'O {var_num} é ímpar!')
elif var_choice == 'Não':
    print('Ok, saindo!')
else:
    print('Error001: valor inválido!')