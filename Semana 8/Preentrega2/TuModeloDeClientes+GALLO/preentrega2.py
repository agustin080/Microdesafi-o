class Clientes():
    def __init__(self, Nombre, Apellido, Monto, Lugar, Producto):
        self.nombre = Nombre
        self.apellido = Apellido
        self.monto = Monto
        self.lugar = Lugar
        self.producto = Producto
    
    def comprar(self):
        return print(f"El cliente ha comprado de {self.lugar}, el producto {self.producto}")
        
    def __str__(self):
        return "Apellido: " + self.apellido + ", Nombre: " + self.nombre + ", Monto: " + self.monto + ", Lugar: " + self.lugar + ", Producto: " + self.producto
    
    def devolucion(self):
        return print(f"El cliente quiere devolver el producto {self.producto}")
    
#cliente1 = Clientes("José", "Gomez", "20000$", "Walmart","Televisor") 
#print(cliente1)
#cliente2 = Clientes("Álvaro","Rodríguez","5000$","Carrefour","Micrófono")
#print(cliente2)
#cliente1.comprar()
#cliente1.devolucion()