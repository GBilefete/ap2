# encoding: utf-8
import mysql.connector
from FormAluno import FormAluno
from Aluno import Aluno

conn = mysql.connector.connect(host='localhost', database='gymsystem', user='root', password='')
if conn.is_connected():
    form = FormAluno()
    aluno = form.show()

    #print(aluno.__repr__())
    #quit()

    if aluno != None:

        try:

            query = "INSERT INTO alunos (nome, CPF, email, modalidades, sexo, telefone_res, telefone_celular, data_nascimento, endereco, observacoes, status) VALUES ("
            query += " '" + aluno.nome + "' , '" + aluno.getCPF() + "' , '" + aluno.email + "' , '" + aluno.modalidades + "' , '" + aluno.sexo + "' , '" + aluno.fone_res + "' , '" + aluno.fone_cel + "' , '" + aluno.data_nasc + "' , '" + aluno.endereco + "' , '" + aluno.obs + "' , '" + aluno.status + "')"
            

            #print(query)
            print("Cadastro concluído com sucesso!")

            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()

            #last_id = cursor.lastrowid
            #print(last_id) 

            cursor.close()
            conn.close()

        except:
            print("Erro ao cadastrar o aluno!")
else: 
    print("Não foi possível conectar ao banco")