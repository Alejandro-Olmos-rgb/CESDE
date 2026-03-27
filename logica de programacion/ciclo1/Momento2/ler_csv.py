import csv

print("Leer archivo")

inventario = []

try:
    with open("Equipos.csv", mode = "r") as f:
        lector = csv.reader(f, delimiter="")
        for fila in lector:
            print(f"Leyendo la fila ... {fila[1]}")
            inventario.append(fila)
            print(f"archivo cargando con exito. {len(inventario)}")

except:
    pass