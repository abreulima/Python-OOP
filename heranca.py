class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"{self.modelo} está ligando...")

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)  # Chamando o construtor da classe base
        self.portas = portas

    def abrir_porta(self):
        print(f"Abrindo uma das {self.portas} portas do {self.modelo}.")

# Criando um objeto da classe Carro
carro = Carro("Toyota", "Corolla", 4)

# Usando métodos da classe base e da classe derivada
carro.ligar()          # Método herdado
carro.abrir_porta()    # Método específico da classe Carro
