import mysql.connector
conn = mysql.connector.connect(host='localhost', database='gymsystem', user='root', password='')

class Modalidade:

    def __init__(self, nome = None):
        self.id = None
        self.nome = nome

    def getMod(self):
        
        modalidades = {}

        if conn.is_connected():

            cursor = conn.cursor()
            cursor.execute("SELECT id, nome FROM modalidade ORDER BY id")
            result = cursor.fetchall()

            for mod in result:
                modalidades[mod[1]] = mod[0]

            cursor.close()
            conn.close()
    
        return modalidades
            