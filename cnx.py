import mysql.connector

def conectar():
    try:
        camino = mysql.connector.connect(host="127.0.0.1",
                                        user="root",
                                        password="123456789",
                                        database="floristeria", 
                                        port="3306")
        if camino.is_connected():
            print("Conexcion exitosa")
            return camino
    except mysql.connector.Error as er:
        print("Error", er)

camino = conectar()