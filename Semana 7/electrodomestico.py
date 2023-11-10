class electrodomestico():
    def __init__(self, precio, Marca, Modelo):
        self.marca = Marca
        self.modelo = Modelo
        self.precio = precio
    
class televisor(electrodomestico):
    def __init__(self, precio, Marca, Modelo, Resolucion = 20, SintonizadorTDT = False):
        super().__init__(precio, Marca, Modelo)
        self.res = Resolucion
        self.sint = SintonizadorTDT

    def preciofinal(self):
        lista = [self.precio]
        if self.res > 40:
            lista.append(self.precio*0.3)

        if self.sint == True:
            lista.append(50)

        print("El precio final es: $", sum(lista)) 
    
    def __str__(self):
        return "Marca: " + self.marca + " ,Modelo: " + self.modelo

class lavadora(electrodomestico):
    def __init__(self, precio, Marca, Modelo, Carga = 5):
        super().__init__(precio, Marca, Modelo)
        self.carga = Carga
    
    def preciofinal2(self):
        lista2 = [self.precio]
        if self.carga > 30:
            lista2.append(50)
        print("El precio final es: $", sum(lista2))

    def __str__(self):
        return "Marca: " + self.marca + " ,Modelo: " + self.modelo


tele1 = televisor(20, "Honda", "R5", 50, True)
tele1.preciofinal()
print(tele1)
lava1 = lavadora(30, "Hyundai", "X2", 60)
lava1.preciofinal2()
print(lava1)



