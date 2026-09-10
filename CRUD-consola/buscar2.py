import mysql.connector 
from cnx import conectar

try:
    camino = conectar()

    carrito = camino.cursor()
    consulta = "SELECT * FROM alumnos WHERE idalumno =%s"""
    datos =[1]
    carrito.execute(consulta, datos)
    registros = carrito.fetchall() #sirve para obtener los registros que se encuentran en una tabla de una BD

    for filas in registros:
        print(filas[0], filas[1], filas[2])
except mysql.connector.Error as e:
    print("Problemas", e)

finally:
    carrito.close()
    camino.close()