def tabla(numero, terminos=10):
    for x in range(terminos):
        va=x*numero
        if (x==terminos-1):
            print(va, " " ,end=' ')
        else:
            print(va," ", sep=",",end=" ")
    print()
    

# bloque principal

print("Tabla del 3")
tabla(3)
print("Tabla del 3 con 5 terminos")
tabla(3,5)
print("Tabla del 3 con 20 terminos")
tabla(terminos=20,numero=3)
