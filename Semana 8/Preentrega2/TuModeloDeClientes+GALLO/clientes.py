from preentrega2 import Clientes

cliente1 = Clientes("José", "Gomez", "20000$", "Walmart","Televisor") 
print(cliente1)
cliente2 = Clientes("Álvaro","Rodríguez","5000$","Carrefour","Micrófono")
print(cliente2)
cliente1.comprar()
cliente1.devolucion()