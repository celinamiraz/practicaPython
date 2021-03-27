#Escriba un programa que solicite se ingrese una palabra o frase 
# y permita identificar si la misma es un heterograma
#Tener en cuenta: No se puede repetir solo caracteres letras
#no distingue may y min

frase = input("Ingresar palabra o frase a identificar")
heterograma = True
for letra in frase:
    if letra.isalpha():
        if frase.lower().count(letra) > 1:
            heterograma = False
            break
if heterograma:
    print(f"La palabra o frase ingresada: {frase} es un Heterograma")
else:
    print(f"La palabra o frase ingresada: {frase} NO es un Heterograma")
