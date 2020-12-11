class Aluno:

    def __init__(self, nome = None, cpf = None, email = None, modalidades = None, sexo = None, fone_res = None, fone_cel = None, data_nasc = None, endereco = None, obs = None, status = None):
        self.__matricula = None
        self.nome = nome
        self.__cpf = cpf
        self.email = email
        self.modalidades = modalidades
        self.sexo = sexo
        self.fone_res = fone_res
        self.fone_cel = fone_cel
        self.data_nasc = data_nasc
        self.endereco = endereco
        self.obs = obs
        self.status = status

    def getMat(self):
        return self.__matricula
    
    def getCPF(self):
        return self.nome

    def setCPF(self, cpf):
        self.__cpf = cpf