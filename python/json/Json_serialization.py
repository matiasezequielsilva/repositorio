#Crear un json file y mostrarlo en pantalla
import json
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_dir)

data = {
    "users":[{ 
        "name": "Maria Jose",
        "age": 34
    },
    {
        "name": "Matias",
        "age": 32
    }]
}

with open("data_file.json", "w") as write_file:
    #Serialization(de objeto python a json)
    json.dump(data, write_file, indent=4)
#dumps es para transformarlo en un string
json_str = json.dumps(data, indent=4)
print(json_str)