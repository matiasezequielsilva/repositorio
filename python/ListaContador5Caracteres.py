lista=["Carlos", "Juan", "Pedro", "Mario", "Luis"]
contador=0
for i in range (len(lista)):
    if len(lista[i])>=5:
        contador=contador+1
print("Los nombres son:")
print(lista)
print("Cantidad de nombres que superan los 5 caracteres:")
print(contador)
