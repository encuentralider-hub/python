ws_nombre = "Duval"
db_nombre_usuario = ""
ws_contraseña_almacenada_en_bd = "Admin1234"
ws_contraseña_tipeada_por_usuario = "Admin1235"
ws_ingreso_valido = ws_contraseña_almacenada_en_bd == ws_contraseña_tipeada_por_usuario
print (ws_ingreso_valido)

if ws_ingreso_valido :
    if db_estatus=="activo":
        
    print ("Contraseña correcta")
    print ("Bienvenido" , ws_nombre) 
if ws_ingreso_valido :
    print ("Contraseña correcta")
#else
else:
    print ("Error, Contraseña incorrecta")

ws_sueldo_mensual=10000
ws_gastos_mensual=2000
if ws_sueldo_mensual >= 10000:
    if ws_gastos_mensual < 2000:
        print("Estas economicamente bien en cualquier parte del mundo")
    else:
        print("Estas economicamente bien en cualquier parte del mundo pero estas gastando mucho")
elif ws_sueldo_mensual >= 5000:
    print("Estas economicamente bien en latinoamerica")
elif ws_sueldo_mensual >= 3000:
    print("Estas economicamente bien en Ecuador")
else:
     print("Debes aprender Phyton")