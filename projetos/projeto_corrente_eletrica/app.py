from math import sqrt

var_choice = input('Deseja converter para descobrir a corrente elétrica? Sim? ou Não? ')

if var_choice == 'Sim':
    var_choice = input('Como você deseja converter? Tensão e Resistência? Tensão e Potência? ou Potência e Resistência? ')

    if var_choice == 'Tensão e Resistência': 
        var_tensao = float(input('Digite a Tensão em Volts: '))
        var_resistencia = float(input('Digite a Resistência em Ohms: '))

        var_amper = var_tensao / var_resistencia

        print(f'A corrente elétrica é de {var_amper}A')
    elif var_choice == 'Tensão e Potência': 
        var_tensao = float(input('Digite a Tensão em Volts: '))
        var_potencia = float(input('Digite a Potência em Watts: '))

        var_amper = var_potencia / var_tensao 

        print(f'A corrente elétrica é de {var_amper}A')
    elif var_choice == 'Potência e Resistência': 
        var_potencia = float(input('Digite a Potência em Watts: '))
        var_resistencia = float(input('Digite a Resistência em Ohms: '))

        var_amper = sqrt(var_potencia / var_resistencia)

        print(f'A corrente elétrica é de {var_amper:.2}A')
    else:
        print('Error002: unexpected_value!')
elif var_choice == 'Sim':
    print('Ok, Saindo!')
else: 
    print('Error001: null_value or invalid_value!')