#Dada una frase y un string ingresados por teclado (en ese orden), 
# genere una lista de palabras,y sobre ella, 
# informe la cantidad de palabras en las que se encuentra el string. 
# No distingirentre mayúsculas y minúsculas.

frase = input("Ingresar frase:")
palabra = input("Ingresar palabra a buscar:")
lista = frase.split(" ")
cantidad = 0
for elem in lista:
    if palabra.lower() == elem.lower():
        cantidad = cantidad + 1
print(f"La palabra '{palabra}' aparece {cantidad} veces en la frase")


