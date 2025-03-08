class Forma:
    def area(self):
        raise NotImplementedError("O método 'area' precisa ser implementado nas subclasses")

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2

# Criando objetos das classes concretas
retangulo = Retangulo(10, 5)
circulo = Circulo(7)

# Acessando a área de cada forma
print("Área do retângulo:", retangulo.area())  # Saída: 50
print("Área do círculo:", circulo.area())      # Saída: 153.86
