print("1. Soy un string - 4")
print("2. 4/0")
print("3. prnt(Mostrando código)")
print("4. int(Quiero ser un número.)")

tipo = int(input("Seleccionar el tipo de error que desee mostrar: "))

if tipo == 1:
    try:
        "Soy un string" - 4
    except TypeError:
        print("Hubo un error con los tipos de dato.")

if tipo == 2:
    try:
        4/0
    except ZeroDivisionError:
        print("No se puede dividir por 0")

#if tipo == 3:
 #   try:
  #      prnt("asdasd")
   # except NameError:
    #    print("Cógido mal escrito")

if tipo == 4:
    try:
        int("Quiero ser un número")
    except ValueError:
        print("No puede convertirse en entero.")