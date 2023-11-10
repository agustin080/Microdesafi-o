BaseDatos = {}
def registro():
    BaseDatos[nombre_de_usuario] = contrasena
    return print("Usuario y contraseña registrados.")

def mostrar():
    return print("La base de datos almacenada es: ",BaseDatos)

def login():
    a = input("Ingrese nombre de usuario: ")
    for i in BaseDatos.keys():
        if i == a:
            b = input("Ingrese contraseña: ")
            for j in BaseDatos.values():
                if  j == b:
                    print("Usuario y contraseña correctos.")
                else:
                    print("Contraseña incorrecta")
        else:
            print("Usuario incorrecto")
    return

#Se podrán registrar nombres de usuarios y contraseña hasta que el usuario escriba la letra "n"
while True:
    nombre_de_usuario = input("Ingrese un nombre de usuario: ")
    if nombre_de_usuario == "n":
        print("Registros terminados.")
        break
    else:
        contrasena = input("Ingrese una contraseña: ")
        registro()
login()
mostrar()
