ws_dictionary = {
    "nombre" : "Duval",
    "apellido": "Molina",
    "sueldo": 10000
}
print(ws_dictionary)
ws_claves = ws_dictionary.keys() #nos devuelve un objeto tipo doct_item que se puede iterar

ws_nombre = ws_dictionary.get("nombre")
ws_sueldo = ws_dictionary.get("sueldos") #con get si no lo encuentra la clave sale none, no sale excepcion ni corta el programa, eso sale si no usamos get sino directamente el nombre de la clave con corchetes y no la encuentra
print(ws_claves,ws_nombre,ws_sueldo)

print("voy a obtener un objeto tipo dict_item que se puede iterar con el metodo items():")
ws_iterar = ws_dictionary.items()
print(ws_iterar)


print("ahora voy a borrar el dato sueldo del diccionario:")
ws_dictionary.pop("sueldo")
print(ws_dictionary)

print("ahora voy a borrar otro dato del diccionario:")
# ws_dictionary.pop("sueldo") #este ya no existe
ws_dictionary.pop("nombre")
print(ws_dictionary)

print("ahora voy a borrar los datos del diccionario:")
ws_dictionary.clear() #borra datos del diccionario
print("como ven, ya esta borrado los datos:", ws_dictionary)