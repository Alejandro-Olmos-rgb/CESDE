producto = {
    "Nombre" : "Teclado",
    "Precio" : 100000.00,
    "Stock" : 5,
    "Tag" : ["Refresco", "Gaseosas", "Bebida", [1232,343]],
    "Categoria" : "Bebidas"
}
producto["descripcion" ] = "Bebida carbonatada de sabor unico"
print(producto["tag"])

del producto["tag"]
print(producto)