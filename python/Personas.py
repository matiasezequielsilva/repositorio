def carga():
    documentos={}
    for i in range(4):
        documento=int(input("ingrese un documento: "))
        nombre=input("ingrese nombre y apellido: ")
        documentos[documento]=nombre
    return documentos

def muestraCompleta(documentos):
    for documento in documentos:
        print(documento,documentos[documento])

def persona(documentos):
    doc=0
    doc=int(input("ingrese el documento de la persona que desea buscar: "))
    if doc in documentos:
        print(doc,documentos[doc])
    else:
        print("No se encontro a la persona")
        respuesta='y'
        respuesta=input("desea buscar otra? s/n")
        while respuesta != 's' and respuesta != 'n':
            print("debe responder s para SI y n para NO")
            respuesta=input("desea buscar otra? s/n ")

        if respuesta=='s':
            persona(documentos)

documentos=carga()
muestraCompleta(documentos)
persona(documentos)
