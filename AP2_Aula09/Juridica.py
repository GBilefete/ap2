from Pessoa import Pessoa

class Juridica(Pessoa):

    def __init__(self, codigoP, nomeP, enderecoP, telefoneP, cnpj, inscricaoEstadual, quantidadeFuncionarios):
        super().__init__(codigoP, nomeP, enderecoP, telefoneP)
        self.__cnpj = cnpj
        self.__inscricaoEstadual = inscricaoEstadual
        self.quantidadeFuncionarios = quantidadeFuncionarios

    def imprimeCNPJ(self):
        print("CNPJ: " + self.__cnpj)

    def __emitirNotaFiscal(self):
        print("NF: " + self.__inscricaoEstadual)

    def getNF(self):
        return self.__emitirNotaFiscal()
