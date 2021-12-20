def cargar():
    lista=[]
    for i in range(5):
        valor=int(input("cargar numero: "))
        lista.append(valor)
    return lista
def imprimir(lista):
    
    for elemento in lista:
        print ("lista completa", elemento)
def mayor(lista):
    mayor=lista[0]
    for elemento in lista:
        if elemento>mayor:
            mayor=elemento
    print("el mayor numero de la lista es: ", mayor)
    return mayor
def suma(lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    print("la suma de los elementos es: ", suma)
    return suma

lista=cargar()
imprimir(lista)
mayor(lista)
suma(lista)


