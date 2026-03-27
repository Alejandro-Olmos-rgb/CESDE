import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="la_colmenita"
)
cursor = db.cursor()

def menu_productos():
    while True:
        print("\nTABLA PRODUCTOS")
        print("1. Ver | 2. Agregar | 3. Volver")
        opc = input("Selecciona: ")
        if opc == "1":
            cursor.execute("SELECT * FROM productos")
            for f in cursor.fetchall(): print(f)
        elif opc == "2":
            nom = input("Nombre: "); desc = input("Descripcion: "); mar = input("Marca: ")
            cursor.execute("INSERT INTO productos (nombre_producto, descrip_producto, marca ) VALUES (%s, %s, %s)", (nom, desc, mar))
            db.commit()
        elif opc == "3": break

def menu_clientes():
    while True:
        print("\nTABLA CLIENTES")
        print("1. Ver | 2. Agregar | 3. Volver")
        opc = input("Selecciona: ")
        if opc == "1":
            cursor.execute("SELECT * FROM clientes")
            for f in cursor.fetchall(): print(f)
        elif opc == "2":
            nombre = input("Nombre: "); apellido = input("apellido: "); tel = input("Teléfono: "); email = input("email: "); mensaje = input("mensaje: ")
            cursor.execute("INSERT INTO clientes (nombre, apellido, telefono, correo, mensaje) VALUES (%s, %s, %s, %s, %s)", (nombre,apellido, tel,email,mensaje ))
            db.commit()
        elif opc == "3": break

while True:
    print("\nLA COLMENITA")
    print("Gestion Administrativa")
    print("1. Gestionar Productos")
    print("2. Gestionar Clientes")
    print("3. Salir")
    
    principal = input("Elige una tabla: ")

    if principal == "1":
        menu_productos()
    elif principal == "2":
        menu_clientes()
    elif principal == "3":
        print("Saliendo...")
        break

db.close()