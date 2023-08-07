var_valor = float(input('Insira um valor: '))
var_taxa_juros = float(input('Insira uma taxa de juros a.a: '))
var_tempo = int(input('Insira o tempo em anos: '))

montante = var_valor * (1 + var_taxa_juros/100)**var_tempo

print(f'O montante ao final do investimento será de R${round(montante, 2)}')