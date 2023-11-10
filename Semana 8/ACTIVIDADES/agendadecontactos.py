import json

data = {}

def registro():
    n = input("Ingrese cantidad de usuarios: ")
    n = int(n)
    for i in range(n): 
        data["Nombre"] = [input("Ingrese Nombre: ")]
        data["Apellido"] = [input("Ingrese Apellido: ")]
        data["Teléfono"] = [input("Ingrese Teléfono: ")]
        data["Dirección"] = [input("Ingrese Dirección: ")]
    return print("Usuarios registrados.")

def imprimir():
    m = input("Ingrese nombre: ")
    l = input("Ingrese apellido: ")
    for key, value in data.items():
        if m == data.keys() and l == data.keys():
            print("xd")
    return

registro()