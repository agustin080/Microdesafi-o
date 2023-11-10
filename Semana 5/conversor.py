lista = []
def ordenar(*args):
    lista = list(args)
    if len(lista) == 3:
        lista[0] = lista[0] * 1000
        lista[1] = lista[1] * 10
        print(lista)
    
    elif len(lista) == 1:
        a = lista[0] / 1000
        b = lista[0] / 10
        c = lista[0]
        lista2 = [a, b, c]
        print(lista2)

    return

ordenar(3,4,5)