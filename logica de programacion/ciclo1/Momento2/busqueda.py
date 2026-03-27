concesionario = [
    {"Marca":"BMW", "Modelo":"S1000RR", "Año":"2025", "Color":"BLANCO"},
    {"Marca":"HONDA", "Modelo":"FIREBLADE", "Año":"2025", "Color":"NEGRO"},
    {"Marca":"KTM", "Modelo":"SUPERDUKE", "Año":"2024", "Color":"NARANJA"}
]

def buscar_vehiculo(lista_carros, marca_busqueda):
    for carro in lista_carros:
        if carro["Marca"].lower() == marca_busqueda.lower():
            return carro
    
    return None

busqueda = input("Que marca esta buscando: \n")
resultado = buscar_vehiculo(concesionario, busqueda)

if resultado != None:
    print(f"Econtrado: {resultado["Marca"]} {resultado["Modelo"]}")
else:
    print("No tenemos ese carro")