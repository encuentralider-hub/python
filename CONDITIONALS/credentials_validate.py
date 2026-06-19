ws_usuario_ingresado=cuadro_txt_ingreso_usuario.value()
ws_password_ingresado=cuadro_txt_ingreso_password.value()

db_usuario= select * from db_usuarios where ws_usuario_ingresado=db_usuario.nombre
db_password=db_usuario.password

if ws_password_ingresado == db_password,
    print("Bienvenido " {db_usuario} "al Sistema")
else
    print("conraseña incorrecta intentelo nuevamente")


