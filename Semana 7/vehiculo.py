class Vehiculo():
    def __init__(self, Marca, Modelo, Color):
        self.marca = Marca
        self.modelo = Modelo
        self.color = Color
    
class Auto(Vehiculo):
    def __init__(self, Marca, Modelo, Color, Motor):
        super().__init__(Marca, Modelo, Color)
        self.motor = Motor

    def tocar_bocina(self):
        return print("El auto tocó bocina.")
    
    def __str__(self):
        return "Marca: " + self.marca + " Modelo: " + self.modelo + " Color: " + self.color + " Motor: " + self.motor
    

class Lancha(Vehiculo):
    def __init__(self, Marca, Modelo, Color, tamaño):
        super().__init__(Marca, Modelo, Color)
        self.tamaño = tamaño

    def virar_a_estribor(self):
        return print("Viró a estribor.")
    
    def virar_a_vabor(self):
        return print("Viró a vabor.")

    def __str__(self):
        return "Marca: " + self.marca + " Modelo: " + self.modelo + " Color: " + self.color + " Tamaño: " + self.tamaño

auto1 = Auto("Toyota", "Corolla", "Gris", "V8")
print(auto1)
auto1.tocar_bocina()

lancha1 = Lancha("Honda", "3", "Roja", "Grande")
print(lancha1)
lancha1.virar_a_estribor()
lancha1.virar_a_vabor()