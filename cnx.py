import mysql.connector
import os

def conectar():
    try:
        camino = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "127.0.0.1"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", "123456789"),
            database=os.environ.get("DB_NAME", "floristeria"),
            port=os.environ.get("DB_PORT", "3306")
        )
        if camino.is_connected():
            print("Conexcion exitosa")
            return camino
    except mysql.connector.Error as er:
        print("Error", er)

camino = conectar()
