class Alumnos():
    def __init__(self, Nombre, Apellido, Carrera, DNI, Nota, Edad):
        self.Carrera = Carrera
        self.DNI = DNI
        self.Nota = Nota
        self.Apellido = Apellido
        self.Nombre = Nombre
        self.Edad = Edad

    def imprimir(self):
        return print(f"Nombre: {self.Nombre}, Apellido: {self.Apellido}")
    
    def resultado(self):
        nota = int(self.Nota)
        if nota <= 5:
            print("Desaprobado")
        else:
            print("Aprobado")

alumno1 = Alumnos("Agustin", "Gallo", "Ing. Industrial", "41446899", "3", "23")
alumno2 = Alumnos("Jose", "Rodriguez", "Abogacia", "12312312", "8",  "30")

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()