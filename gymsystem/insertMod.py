# encoding: utf-8
import mysql.connector
from FormModalidade import FormModalidade
from Modalidade import Modalidade

conn = mysql.connector.connect(host='localhost', database='gymsystem', user='root', password='')
if conn.is_connected():
    form = FormModalidade()
    modalidade = form.show()

    if modalidade != None:

        try:

            query = "INSERT INTO modalidade (nome) VALUES ("
            query += " '" + modalidade.nome + "')"

            #print(query)
            print("Cadastro concluído com sucesso!")

            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
            conn.close()

        except:
            print("Erro ao cadastrar a modalidade!")
else: 
    print("Não foi possível conectar ao banco")