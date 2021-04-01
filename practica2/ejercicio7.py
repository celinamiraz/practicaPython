# Trabajando con los contenidos de los archvios que pueden acceder en el curso:
# Copiar el contenido de los archvios en variables de tipo string y realizar.
# •generar una estructura con los nombres de los estudiantes y la suma de ambas
# •Calcular el promedio de las notas totales e informar quiénes obtuvieron
# menos que el promedio.notas.

def generar_lista_numeros(string_raw):
    """Genera una lista de enteros a partir de una string separada por comas
     y saltos de linea"""
    lista = string_raw.replace(" ", "").replace("\n", "").split(",")
    lista = [int(nota) for nota in lista]
    return lista
# return list(map(int, string_raw.replace(" ", "").replace("\n", "").split(",")))


def generar_lista(string_raw):
    """Genera lista de strings a partir de una string recibida"""
    list = string_raw.replace(" ", "").replace('"', '').title().split(',\n')
    return list


nombres = """'Agustin',
 'Alan',
 'Andrés',
 'Ariadna',
 'Bautista',
 'CAROLINA',
 'CESAR',
 'David',
 'Diego',
 'Dolores',
 'DYLAN',
 'ELIANA',
 'Emanuel',
 'Fabián',
 'Facundo',
 'Facundo',
 'FEDERICO',
 'FEDERICO',
 'GONZALO',
 'Gregorio',
 'Ignacio',
 'Jonathan',
 'Jonathan',
 'Jorge',
 'JOSE',
 'JUAN',
 'Juan',
 'Juan',
 'Julian',
 'Julieta',
 'LAUTARO',
 'Leonel',
 'LUIS',
 'Luis',
 'Marcos',
 'María',
 'MATEO',
 'Matias',
 'Nicolás',
 'NICOLÁS',
 'Noelia',
 'Pablo',
 'Priscila',
 'TOMAS',
 'Tomás',
 'Ulises',
 'Yanina'
"""
evaluacion_uno = """81,
 60,
 72,
 24,
 15,
 91,
 12,
 70,
 29,
 42,
 16,
 3,
 35,
 67,
 10,
 57,
 11,
 69,
 12,
 77,
 13,
 86,
 48,
 65,
 51,
 41,
 87,
 43,
 10,
 87,
 91,
 15,
 44,
 85,
 73,
 37,
 42,
 95,
 18,
 7,
 74,
 60,
 9,
 65,
 93,
 63,
 74
"""
evaluacion_dos = """30,
 95,
 28,
 84,
 84,
 43,
 66,
 51,
 4,
 11,
 58,
 10,
 13,
 34,
 96,
 71,
 86,
 37,
 64,
 13,
 8,
 87,
 14,
 14,
 49,
 27,
 55,
 69,
 77,
 59,
 57,
 40,
 96,
 24,
 30,
 73,
 95,
 19,
 47,
 15,
 31,
 39,
 15,
 74,
 33,
 57,
 10
"""
lista_nombres = generar_lista(nombres)
notas_uno = generar_lista_numeros(evaluacion_uno)
notas_dos = generar_lista_numeros(evaluacion_dos)
listado_final = {}
promedio = 0
# popular diccionario y calcular promedio
for elem in range(len(lista_nombres)):
    listado_final[lista_nombres[elem]] = notas_uno[elem] + notas_dos[elem]
    promedio += notas_uno[elem] + notas_dos[elem]
promedio /= len(lista_nombres) + len(lista_nombres)
# imprimir estudiantes con promedio menor al promedio general
print("Los estudiantes con promedio menor al general son:")
for elem in listado_final:
    if listado_final[elem] / 2 < promedio:
        print(elem)
