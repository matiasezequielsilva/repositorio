#guerra

sexo=input("ingresar sexo (M para masculino y F para femenino): ")
if sexo=="M":
    edad=int(input("ingresar edad:"))
    if edad >=18 and edad<40:
        print("Va a la guerra")
    else:
        print("No va a la guerra")
else:
    print("No va a la guerra")

