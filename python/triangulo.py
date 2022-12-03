#triangulo
def cargaTriangulo():
    lado=int(input("ingrese el lado del triangulo: "))
    return (lado)
def tipoTriangulo(lado1,lado2,lado3):
    if lado1+lado2<lado3:
        print("Estos lados no conforman un triangulo.")
        lado1=cargaTriangulo()
        lado2=cargaTriangulo()
        lado3=cargaTriangulo()
    if lado1+lado3<lado2:
        print("Estos lados no conforman un triangulo.")
        lado1=cargaTriangulo()
        lado2=cargaTriangulo()
        lado3=cargaTriangulo()
    if lado2+lado3<lado1:
        print("Estos lados no conforman un triangulo.")
        lado1=cargaTriangulo()
        lado2=cargaTriangulo()
        lado3=cargaTriangulo()
    if lado1==lado2 and lado2==lado3:
        print("el triangulo es equilatero")
    else:
        if lado1==lado2 or lado1==lado3 or lado2==lado3:
            print("el triangulo es isosceles")
        else:
            print("el triangulo es escaleno")

lado1=cargaTriangulo()
lado2=cargaTriangulo()
lado3=cargaTriangulo()
tipoTriangulo(lado1,lado2,lado3)
