num1=int(input("Agregue un numero de hasta 3 cifras:"))
if num1<0 or 1000-num1 <=0:
    print("Error, el numero debe tener como maximo 3 cifras")
else:
    if num1<10:
        print("el numero es de una cifra")
    else:
        if num1<100:
            print("el numero es de 2 cifras")
        else:
            print("el numero es de 3 cifras")
