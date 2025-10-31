# LAÇO DE REPETIÇÃO/LOOP  WHILE

# variavle contador recebe 0
contador = 0

# enquanto contador for menor que 10
while contador < 10:
    
    # executa esse bloco de código
    print(contador)
# incrementa  1     
    contador += 1



numero = 0
while numero < 51:
  print(numero)  
  numero +=1



# usando continue - É usado para pular alguma interação, fazer um controle dentro do while

inicio = 0
while inicio < 11:
    inicio +=1
    if inicio == 3:
        continue    
    print(inicio)

# usando o brak - É usado para parar de repetir o bloco de código e encerra aqui
inicio_2 = 0
while inicio_2 < 11:
    inicio_2 += 1
    if inicio_2 == 3:
        break
    print(inicio_2)
