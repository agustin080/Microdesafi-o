ano_de_nacimiento = int(input("Ingrese año de nacimiento: "))

if (1920 <= ano_de_nacimiento <= 1940):
    print("Usted es generación silenciosa")

elif (1946 <= ano_de_nacimiento <= 1964):
        print("Usted es generación Baby Boomer")

elif (1965 <= ano_de_nacimiento <= 1979):
        print("Usted es generación X")

elif (1980 <= ano_de_nacimiento <= 2000):
        print("Usted es generación Y")

elif (2001 <= ano_de_nacimiento <= 2010):
        print("Usted es generación Z")

else:
    print("Usted no pertenece a ninguna generación")
