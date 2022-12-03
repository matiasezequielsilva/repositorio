class Socio:
    def __init__(self):
        self.nombre=input("Ingrese el nombre del socio: ")
        self.antiguedad=int(input("Ingrese los años de antiguedad: "))
class Club:
    def __init__(self):
        self.Socio1=Socio()
        self.Socio2=Socio()
        self.Socio3=Socio()
    def responsabilidad(self):
        if self.Socio1.antiguedad > self.Socio2.antiguedad:
            if self.Socio1.antiguedad > self.Socio3.antiguedad:
                print(f"El socio con mayor antiguedad es: {self.Socio1.nombre}")
            else:
                print(f"El socio con mayor antiguedad es: {self.Socio3.nombre}")
        else:
            if self.Socio2.antiguedad > self.Socio3.antiguedad:
                print(f"El socio con mayor antiguedad es: {self.Socio2.nombre}")
            else:
                print(f"El socio con mayor antiguedad es: {self.Socio3.nombre}")

Club1=Club()
Club1.responsabilidad()