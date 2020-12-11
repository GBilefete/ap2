import mysql.connector
conn = mysql.connector.connect(host='localhost', database='gymsystem', user='root', password='')
if conn.is_connected():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    result = cursor.fetchall()

    for aluno in result:
        texto = str(aluno[0]) + ": " + aluno[1] + " - " + aluno[5] + " - " + aluno[2]
        print(texto)
        print("------------------------")

    cursor.close()
    conn.close()

else: 
    print("Não foi possível conectar ao banco")