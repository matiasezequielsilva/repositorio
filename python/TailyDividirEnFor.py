"""lista1=[0,1,2,3,4,5,6]
print(lista1[-1]) # 6
print(lista1[-2]) # 5"""

def capicua(cadena):
    indice=-1
    iguales=0
    for x in range(0,len(cadena)//2):
        if cadena[x]==cadena[indice]:
            iguales=iguales+1
        indice=indice-1
    print(cadena)
    if iguales==(len(cadena)//2):
        print("Es capicua")
    else:
        print("No es capicua")
    

# bloque principal

capicua("neuquen")
capicua("casa")