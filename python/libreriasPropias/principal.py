#La parte de sys se usa si quiero usar librerias de otra ruta
#import sys
#sys.path.append('d:/repositorio/python/libreriasPropias')
import operacioneslista

lista=operacioneslista.cargar()
operacioneslista.imprimir_mayor(lista)
operacioneslista.imprimir_suma(lista)