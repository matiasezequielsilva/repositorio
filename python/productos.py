def cargaProductos():
    productos={}
    for i in range(5):
        producto=input("Cargue su producto: ")
        precio=int(input("cargue su precio: "))
        productos [producto]=precio
    return productos

def mostrarProductos(productos):
    for producto in productos:
        print(producto, productos[producto])
def caros(productos):
    for producto in productos:
        if productos[producto]>=100:
            print(producto, productos[producto])

listado=cargaProductos()
mostrarProductos(listado)
caros(listado)