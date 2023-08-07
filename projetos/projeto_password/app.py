import random
import string

var_choice = input("Deseja gerar uma senha? ")

if var_choice == 'Sim':
    var_size = int(input('Qual é o tamanho da senha? '))
    var_senha = ''
    var_valores = string.ascii_uppercase + string.ascii_lowercase + string.ascii_letters + string.punctuation + string.digits
    for i in range (var_size):
        var_senha += random.choice(var_valores)
    print(f'A senha gerada é: {var_senha}')
elif var_choice == 'Não':
    print("Ok, Saindo!")
else:
    print("Error: valor inválido")