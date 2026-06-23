ws_usurio_ingresado=input("ingresa nombre de usuario:")

print("ingresaste el usuario:",ws_usurio_ingresado , "Tercer")
print(f"ingresaste el usuario: {ws_usurio_ingresado}")
ws_sueldo=input("ingresa tu sueldo:")
ws_mejor_sueldo = ws_sueldo * 2
print(f"{ws_usurio_ingresado} cuando lo dupliques tendras : {ws_mejor_sueldo}")

ws_mejora=input("ingresa las veces que deseas que tu sueldo se incremente:") 
ws_mejor_sueldo2 = float(ws_sueldo) * int(ws_mejora)

print(f"Mi querido {ws_usurio_ingresado} , esto es lo que vas a ganar si te enfocas bien : {ws_mejor_sueldo2}")

