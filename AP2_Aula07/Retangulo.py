class Retangulo:
    
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcular(self):
        return self.altura * self.largura

    def imprimir(self):
        print("Altura: {}".format(self.altura));
        print("Largura: {}".format(self.largura))
