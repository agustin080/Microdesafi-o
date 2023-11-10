class Televisores():
    def __init__(self, precio = 100, color = "Blanco", consumo = "F", peso = 5):
        self.precio = precio
        self.color = color
        self.consumo = consumo
        self.peso = peso

    def comprobar_consumo(self):
        lista = ["A", "B", "C", "D", "E", "F"]
        if self.consumo.upper not in lista:
            self.consumo = "F"
    
    def comprobar_color(self):
        lista2 = ["BLANCO", "NEGRO", "ROJO", "AZUL", "GRIS"]
        if self.color.upper not in lista2:
            self.color = "Blanco"
    
    def precio_final(self):
        lista_precio = [self.precio]
        if 0 < self.peso <= 19:
            lista_precio.append(10)
        
        elif 20 <= self.peso <= 49:
            lista_precio.append(50)
        
        elif 50 <= self.peso <= 79:
            lista_precio.append(80)
        
        elif self.peso > 80:
            lista_precio.append(100)
        
        if self.consumo == "A":
            lista_precio.append(100)
        
        elif self.consumo == "B":
            lista_precio.append(80)

        elif self.consumo == "C":
            lista_precio.append(60)
            
        elif self.consumo == "D":
            lista_precio.append(50)
            
        elif self.consumo == "E":
            lista_precio.append(30)
            
        elif self.consumo == "F":
            lista_precio.append(10)
        
        print("El precio final es: ", sum(lista_precio))
    
    def __str__(self):
        return "Color: " + self.color + ", Consumo: " + self.consumo

Tele1 = Televisores(250, "Rojo", "E", 10)
Tele2 = Televisores(143, "Negro", "C", 13)
Tele3 = Televisores(54, "Gris", "E", 7)
Tele4 = Televisores(300, "Violeta", "H", 23)
Tele4.comprobar_color()
Tele4.comprobar_consumo()
print(Tele1)

Tele1.precio_final()
Tele2.precio_final()
Tele3.precio_final()
Tele4.precio_final()