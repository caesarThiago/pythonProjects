var_choice = input("O que você deseja calcular? Velocidade Média, Deslocamento ou Intervalo de Tempo: ")

if var_choice == 'Velocidade Média':
    var_deslocamento = int(input("Insira a distância (em metros): "))
    var_intervalo_de_tempo = int(input("Insira o intervalo de tempo (em segundos): "))

    var_media = var_deslocamento / var_intervalo_de_tempo

    print(f"A velocidade média é {round(var_media, 2)} m/s")
elif var_choice == 'Deslocamento':
    var_vel_media = float(input("Insira a velocidade média: "))
    var_inter_tempo = int(input("Insira o intervalo de tempo: "))

    var_deslocamento_result = var_vel_media * var_inter_tempo

    print(f"O deslocamento é de {round(var_deslocamento_result, 2)} m")
elif var_choice == 'Intervalo de Tempo':
    var_deslocamento_2 = int(input("Insira a distância (em metros): "))
    var_vel_media_2 = float(input("Insira a velocidade média: "))

    var_intervalo_de_tempo_result = var_deslocamento_2 / var_vel_media_2

    print(f"O intervalo de tempo é de {round(var_intervalo_de_tempo_result, 2)} s")
else:
    print('Error001: null_value or invalid_value!')
