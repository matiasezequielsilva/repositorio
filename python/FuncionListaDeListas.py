def crearListaDeListas():
    lista=[]
    elementos=int(input("Cuantos elementos tendra la lista:"))
    sub=int(input("Cuantos elementos tendran las sublistas:"))
    for n in range(elementos):
        lista.append([])
        for i in range(sub):
            valor=input("Ingrese valor:")
            lista[n].append(valor)

    print(lista)

crearListaDeListas()
