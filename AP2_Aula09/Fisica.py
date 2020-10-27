from Pessoa import Pessoa

class Fisica(Pessoa):

    def __init__(self, codigoP, nomeP, enderecoP, telefoneP, cpf, idade, peso, altura):
        super().__init__(codigoP, nomeP, enderecoP, telefoneP)
        self.__cpf = cpf
        self.idade = idade
        self.peso = float(peso)
        self.altura = float(altura)

    def imprimeCPF(self):
        return "CPF: " + self.__cpf

    def __calculaIMC(self):
        return float(self.peso / pow(self.altura, 2))

    def getIMC(self):
        return "IMC: {:.1f}".format(self.__calculaIMC())
