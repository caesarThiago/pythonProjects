var_choice = input('Deseja calcular o valor do montante da taxa selic? Sim? ou Não? ')

if var_choice == 'Sim': 
    capital_inicial = float(input('Digite seu capital inicial: '))
    taxa_juros = float(input('Digite a taxa de juros: '))
    tempo_apl = int(input('Digite o tempo (ao mês): '))

    res_total_juros = capital_inicial * (taxa_juros / 100) * tempo_apl
    res_total_final = capital_inicial + res_total_juros 

    print(f'O valor total final é R${res_total_final:.2f}')
elif var_choice == 'Não': 
    print('Ok, Saindo!')
else:
    print('Error001: null_value or invalid_value!')