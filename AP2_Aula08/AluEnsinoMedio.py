from Aluno import Aluno

class AluEnsinoMedio:

    def __init__(self, codigoA, nomeA, matriculaA, anoA):
        Aluno.__init__(self, codigoA, nomeA, matriculaA)
        self.ano = anoA

    def imprimir(self):
        Aluno.imprimir(self)
        print("Ano: {0}".format(self.ano))