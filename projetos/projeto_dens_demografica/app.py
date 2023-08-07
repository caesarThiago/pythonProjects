var_choice = input('Deseja descobrir a densidade demográfica? Sim? ou Não? ')

if var_choice == 'Sim':
    var_pop = float(input('Digite a população total: '))
    var_area = float(input('Digite a área total (em quilometros quadrados): '))

    print(f'A densidade demográfica é de {var_pop / var_area:.2f}km²')
elif var_choice == 'Não': 
    print('Ok, saindo!')
else: 
    print('Error001: null_value or invalid_value!')