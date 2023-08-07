var_name = input("Insira o seu nome:")

if var_name == 'Cassio' or 'Cássio':
    arquivo = open("arquivo_existente.txt", "a")  
    arquivo.write(f"Sr. {var_name} sua pontuacao do exame de gayzisse foi de 100/100")
    print(arquivo)
    arquivo.close()
else:
    print(f"Olá, {var_name}")