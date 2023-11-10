def es_multiplo(a,b):
    if a % b == 0:
        print(a, "es múltiplo de ",b)
    elif b % a == 0:
        print(b, "es múltiplo de ",a)
    else:
        print("Uno no es múltiplo del otro ni viceversa.")
    return

es_multiplo(6,3)
es_multiplo(5,10)
es_multiplo(100,400)