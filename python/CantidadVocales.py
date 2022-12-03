oracion=(input("Escriba su oracion con mayusculas y minusculas para saber su cantidad de vocales:"))
minusculas=oracion.lower()
contador=0
i=0
while i< len(oracion):
    if minusculas[i]=="a" or minusculas[i]=="e" or minusculas[i]=="i" or minusculas[i]=="o" or minusculas[i]=="u":
        contador=contador+1
    i=i+1
print("La cantidad de vocales de tu oracion es:")
print(contador)
