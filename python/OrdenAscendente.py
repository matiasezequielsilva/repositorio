def ordenAscendente(val1, val2, val3):
    lista=[]
    lista.append(val1)
    lista.append(val2)
    lista.append(val3)
    for n in range(2):
        for i in range (2-n):
            if lista[i]>lista[i+1]:
                aux=lista[i+1]
                lista[i+1]=lista[i]
                lista[i]=aux
    print(lista)

def cargarEnteros():
    num1=int(input("Ingrese un entero:"))
    num2=int(input("Ingrese un entero:"))
    num3=int(input("Ingrese un entero:"))
    print("De menor a mayor:")
    ordenAscendente(num1, num2, num3)
cargarEnteros()
        

            
