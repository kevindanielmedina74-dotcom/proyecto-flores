import mysql.connector
from cnx import conectar

camino = conectar()
try:
    carrito = camino.cursor()
    consulta = """
        UPDATE alumnos
        set nombreA =%s,
            apellidoA =%s
        WHERE idalumno=%s"""
    Datos = ("Alexa", "Castillo",4)
    ejecutar = carrito.execute(consulta, Datos)
    camino.commit()
    print("Datos modificados correctamente")
except mysql.connector.Error as ex:
    print("Error", ex)
finally:
    carrito.close()
    camino.close()