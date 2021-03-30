# Dado un texto solicite por teclado una letra e
# imprima las palabras que comienzan con dicha letra.
# En caso que no se haya inrgesado un letra, indique el error.

def es_letra(letra):
    """Recibe str y verifica que sea UNA sola letra"""
    if len(letra) != 1:
        print("Has ingresado mas de una letra")
        return("")
    elif letra.lower() < "a" or letra.lower() > "z":
        print("El caracter que ingresaste no es valido")
        return("")
    else:
        return(letra.lower())


texto = """En un lugar de la Mancha, de cuyo nombre no quiero acordarme, 
no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, 
adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que 
carnero, salpicón las más noches, duelos y quebrantos los sábados, 
lentejas los viernes, algún palomino de añadidura los domingos, 
consumían las tres partes de su hacienda. El resto della 
concluían sayo de velarte, calzas de velludo para las fiestas 
con sus pantuflos de lo mismo, los días de entre semana se 
honraba con su vellori de lo más fino. Tenía en su casa una 
ama que pasaba de los cuarenta, y una sobrina que no llegaba a 
los veinte, y un mozo de campo y plaza, que así ensillaba el 
rocín como tomaba la podadera. Frisaba la edad de nuestro hidalgo con 
los cincuenta años, era de complexión recia, seco de carnes, enjuto 
e rostro; gran madrugador y amigo de la caza. Quieren decir que tenía 
el sobrenombre de Quijada o Quesada (que en esto hay alguna diferencia 
en los autores que deste caso escriben), aunque por conjeturas verosímiles 
se deja entender que se llama Quijana; pero esto importa poco a nuestro cuento; 
basta que en la narración dél no se salga un punto de la verdad.
"""
palabras = texto.split(" ")
letra = ""
while letra == "":
    letra = input("Ingresar una letra para buscar en el texto")
    print(letra)
    letra = es_letra(letra)
    print(letra)
for elem in palabras:
    if elem.startswith(letra) or elem.startswith(letra.upper()):
        print(elem)
