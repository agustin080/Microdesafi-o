def tabla():
    n = int(input("Ingrese un valor para deducir su tabla: "))
    f = open("tabla-n.txt","w")
    lista = [0,1,2,3,4,5,6,7,8,9]
    for i in lista:
        j = lista[i]*n
        f.write(f"{str(j)}\n")
    f.close()
    return

def tabla2():
#    n = int(input("Ingrese un valor para deducir su tabla: "))
    f2 = open("tabla-n.txt","r")
    content = f2.read()
    print(content)
    f2.close()
    return

tabla()
tabla2()