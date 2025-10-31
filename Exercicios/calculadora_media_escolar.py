# etradas de dados
# aprovado
# recuperação
#reprovada

# Recebe o valor das notas
nota_1 = float(input('Nota 1: ')) 
nota_2 = float(input('Nota 2: '))
nota_3 = float(input('Nota 3:'))

# calcula a media das notas
media = (nota_1 + nota_2 + nota_3) / 3

# printando a nota 
print(f'Média fina {media:.2f}')
if media >= 7:
    print('Aprovado(a)')
elif media >= 5:
    print('Recuperação(a)')
else:
    print('Reprovada(a)')
