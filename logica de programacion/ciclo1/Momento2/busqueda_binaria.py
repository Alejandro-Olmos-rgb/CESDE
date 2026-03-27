def busqueda_binaria(lista_ordenada, objetivo):
    limite_izquierdo = 0
    limite_derecho = len(lista_ordenada) - 1

    while limite_izquierdo <= limite_derecho:
        mitad = (limite_izquierdo+limite_derecho) // 2

        if lista_ordenada[mitad] == objetivo:
            return mitad
        elif lista_ordenada[mitad] < objetivo:
            limite_izquierdo = mitad + 1

        else:
            limite_derecho = mitad - 1
    return -1
        
numeros = [10,20,30,40,50,60,70,80,90,100]
posicion = busqueda_binaria(numeros,70)

print(f"El numero 70 esta en la posicion: {posicion}")
