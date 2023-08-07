var_choice = input('Do you want to register your profile: ')

if var_choice == 'Yes': 
    var_name = input('Enter your full name: ')
    var_age = input('Enter your age: ')
    var_height = float(input('Enter your height: '))
    var_weight = float(input('Enter your weight: '))

    print(f'Your name is {var_name}, you are {var_age} year(s), your height is {var_height}m and your weight is {var_weight}kg.')
elif var_choice == 'No': 
    print('Okay, exit!')
else: 
    print('Error001: null_value')