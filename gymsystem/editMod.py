import mysql.connector
conn = mysql.connector.connect(host='localhost', database='gymsystem', user='root', password='')
if conn.is_connected():
    cursor = conn.cursor()
    cursor.execute( "SELECT * FROM modalidade")
    result = cursor.fetchall()

    for mod in result:
        texto = str(mod[0]) + ": " + mod[1]
        print(texto)
        print("------------------------")

    try:
        
        campo_id = input("Digite o id da modalidade que deseja editar: ")
        campo_value = input("Digite o novo valor: ")

        cursor.execute("UPDATE modalidade SET nome = '" + campo_value + "' WHERE id = " + str(campo_id))
        conn.commit()

        cursor.execute("SELECT * FROM modalidade WHERE id = " + str(campo_id))
        result = cursor.fetchall()
        for mod in result:
            print("Id: " + str(mod[0]))
            print("Nome: " + mod[1])
            print("------------------------")

        print("Cadastro alterado com sucesso!")

        cursor.close()
        conn.close()

    except:
        print("Erro ao alterar a modalidade!")

else: 
    print("Não foi possível conectar ao banco")