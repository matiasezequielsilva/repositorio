def cargar():
    productos={}
    continua="s"
    while continua=="s":
        codigo=int(input("Ingrese el codigo del producto:"))
        descripcion=input("Ingrese la descripcion:")
        precio=float(input("Ingrese el precio:"))
        stock=int(input("Ingrese el stock actual:"))
        productos[codigo]=(descripcion,precio,stock)
        continua=input("Desea cargar otro producto[s/n]?")
    return productos


def imprimir(productos):
    print("Listado completo de productos:")
    for codigo in productos:
        print(codigo,productos[codigo][0],productos[codigo][1],productos[codigo][2])
productos=cargar()
imprimir(productos)