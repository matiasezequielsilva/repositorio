class jugador:
    def __init__(self,nombre,puntos):
        self.nombre=nombre
        self.puntos=puntos
    def __str__(self):
        if self.puntos<1000:
            return self.nombre + " PRINCIPIANTE"
        else:
            return self.nombre + " EXPERTO" 
jugador1=jugador("Matias" , 1001)
jugador2=jugador("Sol" , 999)
jugador3=jugador("Facu" , 1000)

print(jugador1)
print(jugador2)
print(jugador3)