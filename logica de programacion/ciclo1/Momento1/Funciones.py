impuesto = 0.19
def calcular_precio(valor):

    precio_total = valor + (valor * impuesto)
    return precio_total

    precio = calcular_precio(10000)
    print(precio)
