lista=[]
cantidad=0
for i in range(4):
    valor=int(input("cargar valor entero:"))
    lista.append(valor)

mayor=lista[0]
for i in range(4):
    if mayor<lista[i]:
        mayor=lista[i]

for i in range(4):
    if mayor==lista[i]:
        cantidad=cantidad+1
if cantidad>1:
    print("El mayor esta repetido")
print("el mayor es:")
print(mayor)
