print("-----------BIENVENIDO A CINECO-----------")
print("-----------------------------------------")
print("-----PELICULAS DISPONIBLES-----")
print("1) AVENGERS\n" \
"2) EL CONJURO\n" \
"3) TOM Y JERRY\n" \
"4) EL TELEFONO NEGRO\n" \
"5) EL CONJURO 2\n" \
"6) SPIDERMAN: NO WAY HOME\n")


try:
    nombre = input("Como te llamas: " ).upper()
    edad = int(input("Ingresa tu edad: (entre 11 años y 90 años) " ))
    saldo = float(input("Saldo disponible: " ))
    tarjetaCineco = input("¿Tienes tarjeta cineco? - 1) SI - 2) NO: " ).lower()
except ValueError:
    print("Datos solicitados incorrectos reintente otra vez")


if edad < 18:
    print("Las peliculas que puedes ver son: \n"
    "1) AVENGERS\n"
    "2) TOM Y JERRY\n"
    "3)SPIDERMAN: NO WAY HOME\n")
    print("Escoge la pelicula a ver: ")
    pelicula = int(input(""))
    if pelicula == 1:
        pelicula = "AVENGERS"
    elif pelicula == 2:
        pelicula = "TOM Y JERRY"
    elif pelicula == 3:
        pelicula = "SPIDERMAN: NO WAY HOME"


elif edad >= 18 or edad < 90:
   print("Las peliculas que puedes ver son:\n " 
   "1) EL CONJURO\n" 
   "2) EL CONJURO 2\n" 
   "3) EL TELEFONO NEGRO\n" 
   "4) AVENGERS\n" 
   "5) TOM Y JERRY\n" 
   "6 SPIDERMAN: NO WAY HOME\n")
   print("Escoge la pelicula a ver: ")
   pelicula = int(input(""))
   if pelicula == 1:
      pelicula = "EL CONJURO"
   elif pelicula == 2:
      pelicula = "EL CONJURO 2"
   elif pelicula == 3:
      pelicula = "EL TELEFONO NEGRO"
   elif pelicula == 4:
      pelicula = "AVENGERS"
   elif pelicula == 5:
      pelicula = "TOM Y JERRY"
   elif pelicula == 6:
      pelicula = "SPIDERMAN: NO WAY HOME"
print("-----------------------------------------------------------------------")


if saldo > 50.0000 and tarjetaCineco == "si":
   combo = "TU COMBO SERA GRANDE CON DESCUENTO DEL 50%"
   print("Le recomendamos hacer una compra de un combo grande para disfrutar mejor de la funcion\n con tu tarjeta CINECO te queda un descuento del 50%! en tus boletas\n ")
elif saldo < 50.000 or saldo > 30.000 and tarjetaCineco == "si":
   combo = "TU COMBO SERA MEDIANO CON DESCUENTO DEL 15%"
   print("Le recomendamos hacer una compra de un combo mediano para disfrutar mejor de la funcion\n con tu tarjeta CINECO te queda un descuento del 15%! en tus boletas\n ") 
elif saldo < 30.000 or saldo > 25.000 and tarjetaCineco == "si":
  combo = "COMBO PEQUEÑO SERA CON DESCUENTO DEL 5%"
  print("Le recomendamos hacer una compra de un combo pequeño para disfrutar mejor de la funcion\n con tu tarjeta CINECO te queda un descuento del 10%! en tus boletas\n ")
elif saldo < 25 and tarjetaCineco == "si":
   combo = "ESTAS SIN COMBO"
   print("no hay combos por menos de $25.000 lo sentimos\n aun puedes disfrutar de la pelicula con un 5% de descuento en tus boletas\n")


if saldo > 50.0000 and tarjetaCineco == "no":
   combo = "CON UN COMBO GRANDE"
   print(" Le recomendamos hacer una compra de un combo grande para disfrutar mejor de la funcion\n ")
elif saldo < 50.000 or saldo > 30.000 and tarjetaCineco == "no":
   combo = "CON UN COMBO MEDIANO"
   print("Le recomendamos hacer una compra de un combo mediano para disfrutar mejor de la funcion\n ") 
elif saldo < 30.000 or saldo > 25.000 and tarjetaCineco == "no":
  combo = "CON UN COMBO PEQUEÑO"
  print("Le recomendamos hacer una compra de un combo pequeño para disfrutar mejor de la funcion\n ")
elif saldo < 25 and tarjetaCineco == "no":
   combo = "ESTAS SIN COMBO"
   print("no hay combos por menos de $25.000 lo sentimos\n ")
print("-----------------------------------------------------------------------")


print(f"Hola {nombre.lower()}, el resumen de su compra a realizar es: {pelicula.lower()}, {combo.lower()}\n Bienvenido disfrute de su funcion :).")


   




  





        







