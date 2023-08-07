import random 

var_choice = input("Deseja gerar um nome falso? ")

if var_choice == 'Sim': 
    var_nome = ['Miguel', 'Gael', 'Maria Alice', 'João', 'Arthur', 'José', 'Helena', 'Alice', 'Theo', 'Laura', 'Davi']
    var_sobrenome = ['Silva', 'Santos', 'Oliveira', 'Souza', 'Rodrigues', 'Ferreira', 'Alves', 'Lima', 'Gomes', 'Costa']
    nome_gerado = random.choice(var_nome) + ' ' + random.choice(var_sobrenome)
    print(f'O nome gerado é {nome_gerado}')
elif var_choice == 'Não': 
    print('Ok, Saindo!')
else: 
    print('Error001: valor inválido!')