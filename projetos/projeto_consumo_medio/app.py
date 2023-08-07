var_choice = input('Deseja descobrir o consumo médio? ')

if var_choice == 'Sim': 
    var_km = float(input('Digite os quilômetros percorridos: '))
    var_litros = float(input('Digite os litros utilizados: '))

    print(f'O consumo médio é de {var_km / var_litros:.2f} km/L')
elif var_choice == 'Não': 
    print('Ok, saindo!')
else: 
    print('Error001: null_value or invalid_value!')