
num = int(input("Ingrese el numero a multiplicar:"))
def multLista(lista, num, multiplos):
    for i in range (len(lista)):
        multiplos.append(lista[i]*num)
    return multiplos

multiplos=[]
lista = [1,4,15,32,0,5]

multLista(lista,num,multiplos)
print(multiplos)
