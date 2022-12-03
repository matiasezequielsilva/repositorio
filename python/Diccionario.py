#Diccionario
def mostrarPaises(poblacion):
    for clave in poblacion:
        print(clave, poblacion[clave])

poblacion={"Argentina":40000, "Venezuela":60000, "Chile":50000, "Peru":200000, "Alemania":90000}
mostrarPaises(poblacion)