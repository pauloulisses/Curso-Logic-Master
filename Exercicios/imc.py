# formula peso / altura ** 2
print('IMC para adultos – Tabela geral (homens e mulheres)\n')
peso = float(input("Digite seu peso atual em kg: ")) # pega o peso
altura = float(input('Digite sua altura atual: ')) # pega altura

imc = peso / (altura ** 2) # calcula peso / altura ** 2

print(f'Seu IMC é {imc:.2f}:') # printo o valor do calculo com apenas 2 casas decimais 

if imc < 18.5: # se imc < 18.5 
    print('Abaixo do peso')
elif imc < 25: # se o if nn for atendido vira para o elif
    print('Peso Normal')
elif imc < 30: # se o elif não for atendido vem pra esse 
    print('Sobre peso') 
elif imc <  35: # se o elif não for atendido vem pra esse 
    print('Obesidade grau I')
elif imc < 40: # se o elif não for atendido vem pra esse 
    print('Obesidade garu II')

else: # caso nem um dos elifs forem atendido caira no else e ecerra 
    print('Obesidade morbita')