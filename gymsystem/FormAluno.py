import PySimpleGUI as gui
from Aluno import Aluno
from Modalidade import Modalidade

class FormAluno:
    def __init__(self):

        mod = Modalidade()
        modalidades = mod.getMod()

        conteudo = [
            [gui.Text("Nome: ", size=(15, 1)), gui.Input(key="txtNome")],
            [gui.Text("CPF: ", size=(15, 1)), gui.Input(key="txtCpf")],
            [gui.Text("E-mail: ", size=(15, 1)), gui.Input(key="txtEmail")],
            [
                gui.Text("Sexo: ", size=(15, 1)), 
                gui.Radio("Feminino", "sexo", key="F") ,
                gui.Radio("Masculino", "sexo", key="M")
            ],
            [gui.Text("Modalidades: ", size=(15, 1)), gui.Listbox(modalidades, size=(20,8), key='_LIST_')],
            [gui.Text("Telefone residencial: ", size=(15, 1)), gui.Input(key="txtFone_res")],
            [gui.Text("Telefone celular: ", size=(15, 1)), gui.Input(key="txtFone_cel")],
            [gui.Text("Data de nascimento: ", size=(15, 1)), gui.Input(key="data_nasc")],
            [gui.Text("Endereço: ", size=(15, 1)), gui.Input(key="txtEndereco")],
            [
                gui.Text("Observações: ", size=(15, 1)), 
                gui.Multiline(size=(43, 5), key="txtObs")
            ],
            [
                gui.Text("Status: ", size=(15, 1)), 
                gui.InputCombo(("Inativo", "Ativo"), size=(20, 1), key="status")
            ],
            [gui.Button("Salvar")]
        ]
        self.tela = gui.Window("Cadastro de Alunos").layout(conteudo)

    def show(self):
        self.button, self.valores = self.tela.Read()

        nome = self.valores["txtNome"]
        cpf = self.valores["txtCpf"]
        email = self.valores["txtEmail"]
        if self.valores["M"]:
            sexo = "M"
        else:
            sexo = "F"
        fone_res = self.valores["txtFone_res"]
        fone_cel = self.valores["txtFone_cel"]
        data_nasc = self.valores["data_nasc"]
        endereco = self.valores["txtEndereco"]
        obs = self.valores["txtObs"]
        status = self.valores["status"]
        
        if len(nome) != 0:
            alun = Aluno()
            alun.nome = nome
            alun.setCPF(cpf)
            alun.email = email
            alun.sexo = sexo
            alun.fone_res = fone_res
            alun.fone_cel = fone_cel
            alun.data_nasc = data_nasc
            alun.endereco = endereco
            alun.obs = obs
            alun.status = status
            return alun
        else:
            return None