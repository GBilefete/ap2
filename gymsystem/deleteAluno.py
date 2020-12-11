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

        matricula = input("Digite a matrícula do aluno que deseja excluir: ")

        cursor.execute("DELETE FROM alunos WHERE Matricula = " + str(matricula))
        conn.commit()

        cursor.execute("SELECT * FROM alunos")
        result = cursor.fetchall()
        for aluno in result:
            texto = str(aluno[0]) + ": " + aluno[1] + " - " + aluno[5] + " - " + aluno[2]
            print( texto )
            print("------------------------")

        print("Aluno excluído com sucesso!")

        cursor.close()
        conn.close()

    except:
         print("Erro ao deletar o aluno!")
else: 
    print("Não foi possível conectar ao banco")