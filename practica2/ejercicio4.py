#Retomamos el código visto en la teoría, que informaba si los caracteres 
# “@” o “!” formaban parte de una palabra ingresada

cadena=input("Ingresa la clave (debe tener menos de 10 caracteres y no contener los símbolos:@ y !):")
if len(cadena) > 10:
    print("Ingresaste más de 10 carcateres")
elif "@" or "!" in cadena:
    print("OOPPSIngresaste alguno de estos símbolos: @ o !")
else:
    print("Ingreso OK")