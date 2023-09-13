#la parte de import os y su uso es necesaria si el workspace de visual studio no coincide con el del archivo
#print("Directorio actual:", os.getcwd())
#Tambien puedo setear la ruta directamente como en current_directory
#current_directory = r'D:\repositorio\python\json'
#Seteandola como workspace con
#os.chdir(current_directory)
#PERO EN ESTE CASO SE TOMA LA RUTA ACTUAL DEL ARCHIVO CON scrpit_dir Y SE SETEA COMO WORKING DIRECTORY
import json
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
print(data)
print(data["users"][1]["name"])