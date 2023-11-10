class alumnos():
    def __init__(self, Nombre, Apellido, Carrera, DNI, Nota, Edad):
        self.Carrera = Carrera
        self.DNI = DNI
        self.Nota = Nota
        self.Apellido = Apellido
        self.Nombre = Nombre
        self.Edad = Edad

    def __str__(self):
        return "Carrera: " + self.Carrera + ", DNI: " + self.DNI + ", Nota: " + self.Nota + ", Apellido: " + self.Apellido + ", Nombre: " + self.Nombre
    
    def estudiar(self):
        print("El Alumno,", self.Nombre, self.Apellido, ", está estudiando.")
    
    def crecer(self):
        self.Edad +=1
        print("El alumno ahora tiene", self.Edad)