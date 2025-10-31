# ESTRUTURA CONDICIONAL

# ESTRUTURA IF =  "SE"

valor = 10
if valor > 5: # sempre tem que ter os dois pontos
    print('O valor é maior que 5.')



# ESTRUTURA ELSE = "SE NÃO"
# ELSE - é utilizado para caso a condição if não for atendida
 # será executada a condição do else
# tem que conveerter para int ou float pq se não fica string
idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('É maior de idade ')
else:
    print('É menor de idade')


# ESTRUTURA ELIF = "SENÃO"

linguagem = input('Digite uma linguagem: ')
if linguagem == 'python':
    print('python é legal!')
elif linguagem == 'java':
    print('java é dificil!')   
elif linguagem == 'cobol':
    print('cobol é antigo!')  
else:
    print('Linguagem não Identificada')       