nombre_alumno = input("Ingrese nombre del alumno: ")
nota = input("Ingrese nota del alumno: ")
materia = input("Ingrese la materia: ")
cadena = nombre_alumno,nota,materia
print(nombre_alumno," ha sacado un ",nota, " en ",materia)

cadena_volteada = cadena[::-1]
print(cadena_volteada)
cadena_formateada = materia[::-1],nota[::-1],nombre_alumno[::-1]
print(cadena_formateada)