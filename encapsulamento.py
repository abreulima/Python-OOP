class Carro:
    def __init__(self, modelo, cor, ano):
        self.__modelo = modelo  # Atributo privado
        self.__cor = cor        # Atributo privado
        self.__ano = ano        # Atributo privado

    # Métodos getter
    def get_modelo(self):
        return self.__modelo

    def get_cor(self):
        return self.__cor

    def get_ano(self):
        return self.__ano

    # Métodos setter
    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_cor(self, cor):
        self.__cor = cor

    def set_ano(self, ano):
        self.__ano = ano

# Criando um objeto da classe Carro
carro = Carro("Fusca", "azul", 1976)

# Acessando os atributos usando getters
print("Modelo:", carro.get_modelo())  # Acessando modelo
print("Cor:", carro.get_cor())        # Acessando cor
print("Ano:", carro.get_ano())        # Acessando ano

# Modificando atributos usando setters
carro.set_modelo("Civic")
carro.set_cor("preto")
carro.set_ano(2022)

# Acessando novamente após modificar
print("\nApós modificações:")
print("Modelo:", carro.get_modelo())
print("Cor:", carro.get_cor())
print("Ano:", carro.get_ano())
