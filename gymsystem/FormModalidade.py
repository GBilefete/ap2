import PySimpleGUI as gui
from Modalidade import Modalidade

class FormModalidade:
    def __init__(self):
        conteudo = [
            [gui.Text("Nome: ", size=(15, 1)), gui.Input(key="txtNome")],
            [gui.Button("Salvar")]
        ]
        self.tela = gui.Window("Cadastro de Modalidade").layout(conteudo)

    def show(self):
        self.button, self.valores = self.tela.Read()

        nome = self.valores["txtNome"]
        
        if len(nome) != 0:
            mod = Modalidade()
            mod.nome = nome
            return mod
        else:
            return None