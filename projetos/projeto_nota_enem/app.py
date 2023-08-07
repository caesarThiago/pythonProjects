var_nota_cht = int(input('Insira sua nota da prova de Ciências Humanas e suas Tecnologias: '))
var_nota_cnt = int(input('Insira sua nota da prova de Ciências da Natureza e suas Tecnologias: '))
var_nota_lct = int(input('Insira sua nota da prova de Linguagens, Códigos e suas Tecnologias: '))
var_nota_mat = int(input('Insira sua nota da prova de Matemática e suas Tecnologias: '))
var_nota_r = int(input('Insira sua nota da Redação: '))


var_media = (var_nota_cht + var_nota_cnt + var_nota_lct + var_nota_mat + var_nota_r) / 5

if var_media >= 600:
    print(f'Sua nota foi de {var_media}, parabens!')
elif var_media < 600:
    print(f'Sua nota foi de {var_media}, tente novamente!')
else:
    print('Error: 4500')
