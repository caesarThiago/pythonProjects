import math

def calculator():
    var_choice = input('Escolha a operação matemática (+, -, *, /, sqrt): ')

    if var_choice == '+': 
        var_num = float(input('Digite um número: '))
        var_num_2 = float(input('Digite outro número: '))
        res_sum = var_num + var_num_2
        print(res_sum)
    elif var_choice == '-': 
        var_num_3 = float(input('Digite um número: '))
        var_num_4 = float(input('Digite outro número: '))
        res_sub = var_num_3 - var_num_4
        print(res_sub)
    elif var_choice == '*':
        var_num_5 = float(input('Digite um número: '))
        var_num_6 = float(input('Digite outro número: '))
        res_multi = var_num_5 * var_num_6
        print(res_multi)
    elif var_choice == '/': 
        var_num_7 = float(input('Digite um número: '))
        var_num_8 = float(input('Digite outro número: '))
        res_div = var_num_7 / var_num_8
        print(res_div)
    elif var_choice == 'sqrt': 
        var_num_9 = float(input('Digite um número: '))
        var_num_10 = float(input('Digite outro número: '))
        res_sqrt = math.sqrt(var_num_9 * var_num_10)
        print(res_sqrt)
    else: 
        print('ErrorReg: CALC001_null_answer')

calculator()