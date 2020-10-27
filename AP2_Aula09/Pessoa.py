class Pessoa:

    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone

    def imprimeNome(self):
        print("Nome: " + self.nome)

    def __imprimeTelefone(self):
        return "Telefone: " + self.__telefone

    def getFone(self):
        return self.__imprimeTelefone()