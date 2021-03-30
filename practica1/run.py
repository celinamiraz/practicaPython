# Dado una letra ingresada por el teclado, queremos saber si es
# mayúscula o minúscula.
letra = input("Por favor ingresar una letra")
while len(letra) != 1:
    letra = input("Ingresar UNA sola letra")
if letra > "a" and letra < "z":
    print(f"La letra ingresada {letra} es minuscula")
elif letra > "A" and letra < "Z":
    print(f"La letra ingresada {letra} es mayuscula")
else:
    print(f"El caracter ingresado {letra} no es una letra")
