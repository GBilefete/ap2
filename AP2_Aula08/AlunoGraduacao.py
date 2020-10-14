from Aluno import Aluno

class AlunoGraduacao:

    def __init__(self, codigoA, nomeA, matriculaA, semestreA):
        Aluno.__init__(self, codigoA, nomeA, matriculaA)
        self.semestre = semestreA

    def imprimir(self):
        Aluno.imprimir(self)
        print("Semestre: {0}".format(self.semestre))