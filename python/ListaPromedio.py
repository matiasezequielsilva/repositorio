lista=[]
bajos=[]
altos=[]
suma=0
promedio=0
i=0
x=0
while i<5:
    altura=float(input("Ingrese una altura:"))
    lista.append(altura)
    suma=suma+altura
    i=i+1
promedio=suma/5
while x<5:
    if lista[x]<promedio:
        bajos.append(lista[x])
    else:
        altos.append(lista[x])
    x=x+1
print ("el promedio es:")
print(promedio)
print("mas bajos que el promedio:")
print(bajos)
print("mas altos que el promedio:")
print(altos)
