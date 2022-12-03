cantidad=0
n=int(input("Cuantas piezas cargara:"))
while 0<=n:
    largo=float(input("Ingrese la medida de la pieza:"))
    if largo>=1.2 and largo<=1.3:
        cantidad=cantidad+1
    n=n-1
print("La cantidad de piezas aptas son")
print(cantidad)
