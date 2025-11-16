class Carro:
    # PROPRIEDADES
    numero_rodas = 4
    quantidade_passageiros = 5



    # FUNÇÕES
    def acelerar(self):
        print('Acelerando sempre uno....')

    def frear(self):
        print('Freando...')

    def buzinar(self):
        print('Buzinando...')   



# HERANÇA
# class Uno está herdando propriedades e funções da class Carro
class Uno(Carro):
    modelo = 'Uno'
    marca = 'Fiat'
    ano = '1992'

# instanciando a class Uno
uno = Uno()
uno.acelerar()
uno.frear()
uno.buzinar() 
print(uno.marca)
print(uno.numero_rodas)
print(uno.quantidade_passageiros)
