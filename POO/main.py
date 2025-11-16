# propriedades
# marca, modelo, cor, tem_câmera, bateria

# Funções
# fazer_ligação, jogar_cobrinha, desperta


class Celular:
    # propriedades
    marca = 'Nokia'
    modelo = 'Tijolão'
    cor = 'Azul'
    tem_camera = False
    bateria = 'Infinita'


    # Funções
    # self é obrigatorio pois é uma instancia da propria classe
    def fazer_ligações(self):
        print('Ligando...')

    def jogar_cobrinha(self):
        print('jogando cobrinha....')

    def despertando(self):
        print('Despertando...')    

    def clcular(self, v1, v2):
        return v1 + v2      

 # instanciando(criando objetos)
celular = Celular()  

# invocando(propriedades)
print(celular.marca)
print(celular.cor)
print(celular.modelo)
print(celular.bateria)
print(celular.tem_camera)


# invocando funções
celular.fazer_ligações()
celular.jogar_cobrinha()
celular.despertando()

calculado = celular.clcular(2, 4)
print(calculado)