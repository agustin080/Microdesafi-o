def division(a,b):
    try:
        a = int(a)
        b = int(b)
        return print("El cociente es: ", a/b)
    except Exception as error:
        print("Es imposible hacer el cociente por: ",error)
    
a = input("Ingrese un número: ")
b = input("Ingrese otro nuúmero: ")

division(a,b)