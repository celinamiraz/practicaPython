#Con la información de los archivos de texto que se encuentran disponibles en el curso:
# •nombres_1
# •nombres_2
# Nota: Trabaje con los datos en variables de tipo string.
# •Indique los nombres que se encuentran en ambos.
# Nota: pruebe utilizando list comprehen-sion.
# •Genere dos variables con la lista de notas que se incluyen en los archivos:
# nombres_1,eval1.txtyeval2.txt e imprima con formato los nombres 
# de los estudiantes con las correspondientesnota y la suma de ambas como se ve en laimagen

def generar_lista(string_recibida):
    """Genera lista de strings a partir de una string recibida"""
    lista_temporal = string_recibida.split(",\n")
    lista_devolver = []
    for elem in lista_temporal:
        lista_devolver.append(elem.replace("'", "").strip().capitalize())

    return lista_devolver

def generar_lista_numeros(string_recibida):
    """Genera una lista de enteros a partir de una string separada por comas y saltos de linea"""
    lista_temporal = string_recibida.split(",\n")
    lista_devolver = []
    for elem in lista_temporal:
        lista_devolver.append(int(elem)) 
    return lista_devolver

nombres1 = """'Agustin',
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
nombres2 = """'Agustin',
 'AGUSTIN',
 'Agustín',
 'Ailen',
 'Alfredo',
 'Amalia',
 'Ariana',
 'Bautista',
 'Braian',
 'Carla',
 'CESAR',
 'Daniel',
 'Diego',
 'ELIANA',
 'Facundo',
 'Facundo',
 'Facundo',
 'Facundo',
 'Federico',
 'Federico',
 'Flavia',
 'Francisco',
 'Germán',
 'Guido',
 'GUSTAVO',
 'Hilario',
 'Ignacio',
 'IVAN',
 'Jimmy',
 'Joaquín',
 'Jose',
 'Josue',
 'JUAN',
 'Juan',
 'Laura',
 'LAURA',
 'Lautaro',
 'Lautaro',
 'Ludmila',
 'Marcos',
 'Marcos',
 'MARIANELA',
 'MARTIN',
 'MATEO',
 'Mateo',
 'Matias',
 'MAURO',
 'Maximiliano',
 'NESTOR',
 'Nicolas',
 'Pedro',
 'Ramiro',
 'Sofía',
 'Tobias',
 'Tomás',
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

lista_nombres1 = generar_lista(nombres1)
lista_nombres2 = generar_lista(nombres2)
lista_notas_uno = generar_lista_numeros(evaluacion_uno)
lista_notas_dos = generar_lista_numeros(evaluacion_dos)
lista_repetidos = [nombre for nombre in lista_nombres1 if nombre in lista_nombres2]
print("Este es el listado de los nombres repetidos:")
print(lista_repetidos)
print("*"*30)
listado_notas_finales = []
for elem in range(len(lista_nombres1)):
    listado_notas_finales.append((lista_notas_uno[elem], lista_notas_dos[elem], lista_notas_uno[elem] + lista_notas_dos[elem]))
print("Nombre".center(15), "Eval1".center(35), "Eval2".center(25), "Total".center(55))
for elem in range(len(listado_notas_finales)):
    print(str(elem).rjust(3), str(lista_nombres1[elem]).ljust(10), str(listado_notas_finales[elem][0]).rjust(20), str(listado_notas_finales[elem][1]).rjust(30), str(listado_notas_finales[elem][2]).rjust(40))
