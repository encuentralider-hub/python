ws_division1 = 12/5 #nos devuelve un dato flotante float
ws_division2 = 12/2 #siempre nos devuelve un dato flotante float
ws_exponente1 = 5**3
ws_divbaja1 = 12//5 #devuelve dato int
ws_resto1 = 12 % 4 #devuelve dato int
ws_tipo = type(ws_resto1)


print(ws_exponente1, ws_division1, ws_division2, ws_resto1, ws_divbaja1, ws_tipo)

ws_igual = ws_divbaja1 == ws_resto1
ws_no_igual = ws_divbaja1 != ws_resto1
ws_contraseña_almacenada_en_bd = "Admin1234"
ws_contraseña_tipeada_por_usuario = "Admin1234"
ws_ingreso_valido = ws_contraseña_almacenada_en_bd == ws_contraseña_tipeada_por_usuario
print (ws_igual, ws_no_igual, ws_ingreso_valido)
