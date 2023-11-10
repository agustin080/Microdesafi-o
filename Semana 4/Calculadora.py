numero1 = int(input("Ingrese el 1° número: "))
numero2 = int(input("Ingrese el 2° número: "))

print("""Opción1: sumar\nOpción2: restar\nOpción3: multiplicar\nOpción4: finalizar programa""")




operacion=int(input("Ingrese qué operación quiere realizar: "))

if operacion == 1:
    suma = numero1 + numero2
    print(suma)

elif operacion == 2:
    resta = numero1 - numero2
    print(resta)

elif operacion == 3:
    producto = numero1 * numero2
    print(producto)

elif operacion == 4:
    print("El programa finalizo")