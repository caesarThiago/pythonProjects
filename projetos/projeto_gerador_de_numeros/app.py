import random

var_choice = input('Deseja gerar um número aleátorio? ')

if var_choice == 'Sim':
    var_num = int(input('Digite um número inteiro: '))
    var_num_2 = int(input('Digite outro número inteiro: '))
    var_num_random = random.randint(var_num, var_num_2)

    print(f'O número gerado foi: {var_num_random}')
elif var_choice == 'Não': 
    print('Ok, saindo!')
else: 
    print('Error001: valor_invalido')