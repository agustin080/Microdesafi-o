ganado = 3
empatado = 1
perdido = 0
partidos_totales = 20

nombre_del_equipo = input("Ingrese el nombre del equipo: ")
partidos_ganados = int(input("Ingrese cantidad de partidos ganados: "))
partidos_empatados = int(input("Ingrese cantidad de partidos empatados: "))
partidos_perdidos = int(input("Ingrese cantidad de partidos perdidos: "))
puntaje_total = partidos_ganados*ganado + partidos_empatados * empatado + partidos_perdidos * perdido
promedio = puntaje_total / partidos_totales
print("El puntaje total de ",nombre_del_equipo," es ",puntaje_total)
print("El promedio de puntos de ",nombre_del_equipo, "es ",promedio,)
