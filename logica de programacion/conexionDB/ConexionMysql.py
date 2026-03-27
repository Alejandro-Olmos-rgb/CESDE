import mysql.connector
import csv


def generar_reporte():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="la_colmenita"
        )

        cursor = conexion.cursor()
        consulta = "SELECT * FROM productos"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        print(resultado)
    except:
        print("Error!")

generar_reporte()