def diccionarios ():
    consecionario = []
    motos = {}
    moto = int(input("Cuantas Motos va a agregar: " ))

    for i in range(moto):
        clave = input("Escriba la Marca: " )
        valor = input("Escriba el Modelo: " )
        motos["marca"] = clave
        motos["valor"] = valor
    
    consecionario.append(motos)

    print(motos)
diccionarios()