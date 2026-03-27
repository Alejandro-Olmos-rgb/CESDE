# Conversor de unidades.

def fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin


def main():
   celsius = int(input("Escriba los grados Celsius. (ºC) " ))
   f = fahrenheit(celsius=0)
   k = kelvin(celsius=0)
   print(f"Los grados celsius son {celsius} convertidos a fahrenheit son {f}, convertidos a kelvin son {k}.")



main()

