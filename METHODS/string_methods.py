ws_saludo1="Bienvenidos a una nueva era"
ws_saludo2="La era de la IA"
ws_anio=2026

print(dir(ws_saludo1))
print(dir(ws_anio))
print (ws_saludo2.upper())
ws_resultado = ws_saludo1.lower()
print (ws_resultado)
print (ws_saludo1.find("eraE")) #devuelve posicion de cadena, empezando desde 0, sino la encuentra , devuelve -1
# el espacio tambien es un caracter
#metodo index() igual que find, pero si no encuentra la cadena manda una excepcion, es decir que corta el programa
#isnumeric = "235" aunque sea texto da true
#isalpha = "abc..z" sin espacios ni caracteres especiales
#len es una funcion, no es un metodo, todos los metodos son funciones pero no todas las funciones son metodos
print(len(ws_saludo1))
ws_saludo3=ws_saludo1.replace(" ",";")
print(ws_saludo3)
ws_cadena_separada=ws_saludo3.split(";")
print(ws_cadena_separada)
print(type(ws_cadena_separada))
