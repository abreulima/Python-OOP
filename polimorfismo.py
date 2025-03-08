class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Função que aceita qualquer objeto do tipo Animal
def emitir_som(animal: Animal):
    print(animal.fazer_som())

# Criando objetos
cachorro = Cachorro()
gato = Gato()

# Usando polimorfismo, o mesmo método (fazer_som) se comporta de maneira diferente
emitir_som(cachorro)  # Saída: Au Au!
emitir_som(gato)      # Saída: Miau!
