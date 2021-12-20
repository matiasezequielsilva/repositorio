def cargar():
    lista = []
    for i in range(3):
        valor=int(input("Agregue un valor a la lista:"))
        lista.append(valor)
    return lista
def variacion(lista):
    if (lista[0]>lista[1]):
        if (lista[1]>lista[2]):
            resultado=lista[0] - lista[2]
        else:
            if (lista[0] > lista[2]):
                resultado=lista[0] - lista[1]
            else:
                resultado=lista[2] - lista[1]
    else:
        if(lista[0]>lista[2]):
            resultado=lista[1] - lista[2]
        else:
            if (lista[1]>lista[2]):
                resultado=lista[1] - lista[0]
            else:
                resultado=lista[2] - lista[0]
    print(resultado)
def main():
    variacion(cargar())
main()