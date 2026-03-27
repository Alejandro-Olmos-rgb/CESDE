import csv 

print ("Exportar un csv")

datos = [
    {"serie": "SN001", "marca": "Lenovo", "precio": 120000},
    {"serie": "SN002", "marca": "DELL", "precio": 150000}
]

with open ("Equipos.csv", mode="w", newline="") as f:
    escritor = csv.writer(f)

    escritor.writerow(["numero serie", "marca", "precio"])

    for dato in datos:
        escritor.writerow([dato["serie"], dato["marca"], dato["precio"]])

print("Archivo creado ")