class Animal:

    def emitir_som(self): # self referencia a si mesmo
        print('Qualquer som...')


# Class cachorro herda as propriedades e funções da classe Animal
class Cachorro(Animal):
    # Subscrevendo a função Animal 
    def emitir_som(self):
        print('AU AU ')


# Class Gato herda as propriedades e funções da class Animal
class Gato(Animal):
   # Subscrevendo a função Animal
    def emitir_som(self):
        print('MIAU!')    


# Class Galinha herda as propriedades e funções da Class Animal
class Galinha(Animal):
    # Subscrevendo a função Animal
    def emitir_som(self):
        print('PIU PIU')
        
    


cachorro = Cachorro()
cachorro.emitir_som()

gato = Gato()
gato.emitir_som()

galinha = Galinha()
galinha.emitir_som()

