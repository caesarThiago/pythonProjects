from cryptography.fernet import Fernet

var_choice = input('Deseja criptografar uma mensagem? ')

if var_choice == 'Sim':
    var_texto = input('Digite o texto para ser criptografado: ')
    chave = Fernet.generate_key()
    fernet = Fernet(chave)
    var_cifrado = fernet.encrypt(var_texto.encode())

    print(f'O texto cifrado: {var_cifrado}')

    var_choice_2 = input('Deseja descriptografar a mensagem? ')

    if var_choice_2 == 'Sim':
        texto_decifrado = fernet.decrypt(var_cifrado).decode()
        print(f'O texto decifrado foi: {texto_decifrado}')
    else:
        print('Ok, saindo!')
elif var_choice == 'Não':
    print('Ok, saindo!')
else:
    print('Error001: null_value')

