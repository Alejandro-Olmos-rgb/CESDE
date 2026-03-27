import csv
import os

print("=== LECTOR DE ARCHIVOS CSV ===")

inventario = []

# Mostrar archivos CSV disponibles en la carpeta
archivos = [f for f in os.listdir() if f.endswith(".csv")]

if not archivos:
    print("❌ No hay archivos CSV en la carpeta")
else:
    print("\nArchivos disponibles:")
    for i, archivo in enumerate(archivos, start=1):
        print(f"{i}. {archivo}")

    try:
        opcion = int(input("\nElige un archivo: "))
        nombre_archivo = archivos[opcion - 1]

        with open(nombre_archivo, mode="r", encoding="utf-8") as f:
            lector = csv.reader(f, delimiter=",")
            
            for fila in lector:
                if len(fila) > 1:
                    print(f"Leyendo fila: {fila[1]}")
                else:
                    print(f"Leyendo fila: {fila}")

                inventario.append(fila)

        print(f"\n✅ Archivo cargado con éxito: {nombre_archivo}")
        print(f"Total de filas: {len(inventario)}")

    except ValueError:
        print("❌ Debes ingresar un número válido")
    except IndexError:
        print("❌ Opción fuera de rango")
    except FileNotFoundError:
        print("❌ Archivo no encontrado")
    except Exception as e:
        print(f"❌ Error: {e}")