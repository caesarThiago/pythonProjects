var_choice = input('Deseja descobrir a escala? ')

if var_choice == 'Sim': 
    var_desenho = float(input('Digite a escala/desenho (em cm): '))
    var_real = float(input('Digite a escala real (em cm): '))

    print(f'A escala é de {var_desenho / var_real:.2} cm')
elif var_choice == 'Não': 
    print('Ok, saindo!')
else: 
    print('Error001: null_value or invalid_value!')