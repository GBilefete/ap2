# encoding: utf-8
import mysql.connector
from FormAluno import FormAluno
from Aluno import Aluno

conn = mysql.connector.connect(host='localhost', database='gymsystem', user='root', password='')
if conn.is_connected():
    form = FormAluno()
    aluno = form.show()

    if aluno != None:

        try:

            query = "INSERT INTO alunos (nome, CPF, email, sexo, telefone_res, telefone_celular, data_nascimento, endereco, observacoes, status) VALUES ("
            query += " '" + aluno.nome + "' , '" + aluno.cpf + "' , '" + aluno.email + "' , '" + aluno.sexo + "' , '" + aluno.fone_res + "' , '" + aluno.fone_cel + "' , '" + aluno.data_nasc + "' , '" + aluno.endereco + "' , '" + aluno.obs + "' , '" + aluno.status + "')"

            #print(query)
            print("Cadastro concluído com sucesso!")

            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
            conn.close()

        except:
            print("Erro ao cadastrar o aluno!")
else: 
    print("Não foi possível conectar ao banco")