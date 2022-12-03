class Persona:
    def inicializar(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

def imprimir(persona):
    print("nombre:",persona.nombre)
    print("edad:", persona.edad)

def mayor(persona):
    if persona.edad >=18 :
        print(persona.nombre," es mayor de edad")

persona=Persona()
persona.inicializar("Diego",18)
imprimir(persona)
mayor(persona)
