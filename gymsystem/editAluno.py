import mysql.connector
conn = mysql.connector.connect(host='localhost', database='gymsystem', user='root', password='')
if conn.is_connected():
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM alunos")
    result = cursor.fetchall()

    for aluno in result:
        texto = str(aluno[0]) + ": " + aluno[1] + " - " + aluno[5] + " - " + aluno[2]
        print(texto)
        print("------------------------")

    try:
        matricula = input("Digite a matrícula do aluno que deseja editar: ")

        print("Campos: nome, CPF, email, modalidades, sexo, telefone_res, telefone_celular, data_nascimento, endereco, observacoes, status")

        campo_edit = input("Digite o campo que deseja editar: ")
        campo_value = input("Digite o novo valor do " + campo_edit + ": ")

        cursor.execute("UPDATE alunos SET " + campo_edit + " = '" + campo_value + "' WHERE Matricula = " + str(matricula))
        conn.commit()

        cursor.execute("SELECT * FROM alunos WHERE Matricula = " + str(matricula))
        result = cursor.fetchall()
        for aluno in result:
            print("Matrícula: " + str(aluno[0]))
            print("Nome: " + aluno[1])
            print("CPF: " + aluno[2])
            print("E-mail: " + aluno[3])
            print("Modalidades: " + aluno[4])
            print("Sexo: " + aluno[5])
            print("Telefone residencial: " + aluno[6])
            print("Telefone celular: " + aluno[7])
            print("Data de nascimento: " + str(aluno[8]))
            print("Endereço: " + str(aluno[9]))
            print("Observações: " + aluno[10])
            print("Status: " + str(aluno[11]))
            print("------------------------")

        print("Cadastro alterado com sucesso!")

        cursor.close()
        conn.close()

    except:
        print("Erro ao alterar o aluno!")

else: 
    print("Não foi possível conectar ao banco")