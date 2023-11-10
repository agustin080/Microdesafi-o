class Auto():
    def __init__(self, Marca, Modelo):
        self.marca = Marca
        self.Modelo = Modelo
    
    def __str__(self):
        return "Marca: " + self.marca + ", Modelo: " + self.Modelo

automovil_1 = Auto("Toyota", "Hilux")
print(automovil_1)