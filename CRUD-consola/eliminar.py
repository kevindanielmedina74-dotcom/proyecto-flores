import mysql.connector
from cnx import conectar

camino = conectar()
try:
    carrito = camino.cursor()
    consulta = """
        DELETE from alumnos
        WHERE idalumno = %s """
    Datos = (4,)
    ejecutar = carrito.execute(consulta, Datos)
    camino.commit
    print("Datos eliminados correctamente")
except mysql.connector.Error as ex:
    print("error", ex)
finally:
    carrito.close()
    camino.close()
