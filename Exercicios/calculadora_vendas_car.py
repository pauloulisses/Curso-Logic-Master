# valor, valor gasto, valor vendido

valor_pago = float(input('Valor pago no carro '))
valor_investido = float(input('Valor investido '))
valor_venda = float(input('Valor da venda '))

custo_total = valor_pago + valor_investido
lucro = valor_venda - custo_total

print(f'Custo total R$: {custo_total}')
print(f'Lucro obitido R$: {lucro}')

if lucro > 0:
    print('Resulado: lucro na venda!')
elif lucro < 0:
    print('Resultado: prejuizo na venda! ')
else:
    print('Resultado: Empate')     