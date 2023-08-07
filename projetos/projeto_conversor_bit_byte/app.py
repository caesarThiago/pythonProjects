var_choice = input('Deseja converter (bit para byte) ou (byte para bit): ')

if var_choice == 'bit para byte': 
    var_bit = float(input('Digite a quantidade de bit(s): '))

    var_byte = var_bit / 8

    print(f'O valor de {var_bit} bit(s) para byte(s) é de {var_byte} byte(s)')

elif var_choice == 'byte para bit': 
    var_byte = float(input('Digite a quantidade de byte(s): '))

    var_bit = var_byte * 8

    print(f'O valor de {var_byte} byte(s) para bit(s) é de {var_bit} bit(s)')

else:
    print('Error001: null_value or invalid_value')