import mysql.connector
conn = mysql.connector.connect(host='localhost', database='gymsystem', user='root', password='')
if conn.is_connected():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM modalidade")
    result = cursor.fetchall()

    for mod in result:
        texto = str(mod[0]) + ": " + mod[1]
        print(texto)
        print("------------------------")

    cursor.close()
    conn.close()

else: 
    print("Não foi possível conectar ao banco")