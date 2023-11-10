nombre = input("¿Cómo te llamas?: ")
Preferencia = input("¿Cuál es tu preferencia?: ")

nombre2 = nombre.capitalize()
Preferencia2 = Preferencia.capitalize()

Letras1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
Letras2= ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

if (nombre2[0] in Letras1) and (Preferencia2 == "M"):
    print("Tu grupo es el A")

elif (nombre2[0] in Letras1) and (Preferencia2 == "C"):
    print("Tu grupo es el B")

if (nombre2[0] in Letras2) and (Preferencia2 == "M"):
    print("Tu grupo es el A")

elif (nombre2[0] in Letras2) and (Preferencia2 == "C"):
    print("Tu grupo es el B")