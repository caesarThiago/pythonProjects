import random 

var_choice = input('Deseja gerar uma nome aleátorio? ')

if var_choice == 'Sim':
    with open('nomes.txt', 'r') as file:
        nomes = file.read().splitlines()

    with open('sobrenomes.txt', 'r') as file:
        sobrenomes = file.read().splitlines()

    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)

    print(f'O nome gerado é {nome} {sobrenome}')
elif var_choice == 'Não': 
    print('Ok, saindo!')
else: 
    print('Error001: null_value!')
