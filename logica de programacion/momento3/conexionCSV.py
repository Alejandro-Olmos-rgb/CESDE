import mysql.connector
import csv

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="la_colmenita"
)
cursor = db.cursor()

# ================== FUNCION EXPORTAR CSV ==================
def exportar_tabla_csv(nombre_tabla):
    cursor.execute(f"SELECT * FROM {nombre_tabla}")
    filas = cursor.fetchall()
    columnas = [desc[0] for desc in cursor.description]

    with open(f"{nombre_tabla}.csv", "w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(columnas)
        writer.writerows(filas)

    print(f" Tabla '{nombre_tabla}' exportada a {nombre_tabla}.csv")


def exportar_toda_la_bd():
    cursor.execute("SHOW TABLES")
    tablas = cursor.fetchall()

    for tabla in tablas:
        exportar_tabla_csv(tabla[0])

    print(" Toda la base de datos fue exportada a CSV")


# ================== MENUS ==================
def menu_productos():
    while True:
        print("\nTABLA PRODUCTOS")
        print("1. Ver | 2. Agregar | 3. Exportar CSV | 4. Volver")
        opc = input("Selecciona: ")

        if opc == "1":
            cursor.execute("SELECT * FROM productos")
            for f in cursor.fetchall():
                print(f)

        elif opc == "2":
            nom = input("Nombre: ")
            desc = input("Descripcion: ")
            mar = input("Marca: ")

            cursor.execute(
                "INSERT INTO productos (nombre_producto, descrip_producto, marca) VALUES (%s, %s, %s)",
                (nom, desc, mar)
            )
            db.commit()

        elif opc == "3":
            exportar_tabla_csv("productos")

        elif opc == "4":
            break


def menu_clientes():
    while True:
        print("\nTABLA CLIENTES")
        print("1. Ver | 2. Agregar | 3. Exportar CSV | 4. Volver")
        opc = input("Selecciona: ")

        if opc == "1":
            cursor.execute("SELECT * FROM clientes")
            for f in cursor.fetchall():
                print(f)

        elif opc == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            tel = input("Teléfono: ")
            email = input("Email: ")
            mensaje = input("Mensaje: ")

            cursor.execute(
                "INSERT INTO clientes (nombre, apellido, telefono, correo, mensaje) VALUES (%s, %s, %s, %s, %s)",
                (nombre, apellido, tel, email, mensaje)
            )
            db.commit()

        elif opc == "3":
            exportar_tabla_csv("clientes")

        elif opc == "4":
            break


def menu_exportacion():
    while True:
        print("\nEXPORTAR A CSV")
        print("1. Exportar Productos")
        print("2. Exportar Clientes")
        print("3. Exportar TODA la Base de Datos")
        print("4. Volver")

        opc = input("Selecciona: ")

        if opc == "1":
            exportar_tabla_csv("productos")
        elif opc == "2":
            exportar_tabla_csv("clientes")
        elif opc == "3":
            exportar_tabla_csv("categorias")
        elif opc == "4":
            exportar_toda_la_bd()
        elif opc == "5":
            break

# ================== MENU PRINCIPAL ==================
while True:
    print("\nLA COLMENITA")
    print("Gestion Administrativa")
    print("1. Gestionar Productos")
    print("2. Gestionar Clientes")
    print("3. Exportar a CSV")
    print("4. Salir")

    principal = input("Elige una opción: ")

    if principal == "1":
        menu_productos()
    elif principal == "2":
        menu_clientes()
    elif principal == "3":
        menu_exportacion()
    elif principal == "4":
        print("Saliendo...")
        break

db.close()