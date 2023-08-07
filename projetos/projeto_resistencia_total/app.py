var_choice = input('Deseja calcular a resistência total? ')

if var_choice == 'Sim': 
    var_res_pos = input('Quantas resistências você tem? ')

    if var_res_pos == '3':
        var_res = int(input('Insira o valor em ohms da resistência 1: '))
        var_res_2 = int(input('Insira o valor em ohms da resistência 2: '))
        var_res_3 = int(input('Insira o valor em ohms da resistência 3: '))

        print(f'O total da resitência é {var_res + var_res_2 + var_res_3}Ω')
    elif var_res_pos == '4':
        var_res = int(input('Insira o valor em ohms da resistência 1: '))
        var_res_2 = int(input('Insira o valor em ohms da resistência 2: '))
        var_res_3 = int(input('Insira o valor em ohms da resistência 3: '))
        var_res_4 = int(input('Insira o valor em ohms da resistência 4: '))

        print(f'O total da resitência é {var_res + var_res_2 + var_res_3 + var_res_4}Ω')
    else:
        print('Error002: limit_trespassing!')
elif var_choice == 'Não':
    print('Ok, saindo!')
else: 
    print('Error001: null_value or invalid_value!')