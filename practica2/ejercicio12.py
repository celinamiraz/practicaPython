minas = ['-*-*-','--*--','----*','*----',]

def es_borde(fila,columna):
    """Chequea si la celda a analizar es parte del borde."""
    if fila == 0 or fila+1 == len(minas) or columna == 0 or columna+1 == len(minas[fila]):
        return True
    else:
        return False

def es_esquina(fila,columna):
    """Chequea si la celda a analizar es una de las 4 esquinas."""
    if (fila == 0 or fila+1 == len(minas)) and (columna == 0 or columna+1 == len(minas[fila])):
        return True
    else:
        return False

def procesar_esquina(fila,columna):
    """Cuenta las minas cuando la celda es una esquina."""
    if fila == 0:
        if columna == 0:
            contador = procesar_celda(fila,columna,[-1,0],[-1,0])
        else:
            contador = procesar_celda(fila,columna,[-1,0],[0,1])
    elif columna == 0:
        contador = procesar_celda(fila,columna,[0,1],[-1,0])
    else:
        contador = procesar_celda(fila,columna,[0,1],[0,1])
    return contador

def procesar_borde(fila,columna):
    """Cuenta las minas cuando la celda es parte del borde y no es una esquina."""
    if not es_esquina(fila,columna):
        if fila == 0:
            contador = procesar_celda(fila,columna,[-1,0],[-1,1])
        elif fila +1 == len(minas):
            contador = procesar_celda(fila,columna,[0,1],[-1,1])
        elif columna == 0:
            contador = procesar_celda(fila,columna,[-1,1],[-1,0])
        else:
            contador = procesar_celda(fila,columna,[-1,1],[0,1])
    else:
        contador = procesar_esquina(fila,columna)
    return contador

def buscar_minas(posicion):
    """Busca las minas de cada celda interna o llama a procesos para buscar minas en los bordes."""
    if not es_borde(posicion[0],posicion[1]):
        contador = procesar_celda(posicion[0],posicion[1],[-1,1],[-1,1])
    else: 
        contador = procesar_borde(posicion[0],posicion[1])
    return contador


def procesar_celda(fila,columna, cantidad_fila, cantidad_columna):
    """Busca la minas minas de una celda especifica."""
    contador = 0
    for elem_fila in range(cantidad_fila[0],cantidad_fila[1]+1):
            for elem_col in range(cantidad_columna[0],cantidad_columna[1]+1):
                if minas[fila-elem_fila][columna-elem_col] == "*":
                    contador += 1
    return contador

minas_procesado = []
fila_minas = []
linea = ""
for fila in range(len(minas)):
    for columna in range(len(minas[fila])):
        if minas[fila][columna] == "-":
            fila_minas.append(str(buscar_minas([fila,columna])))
        else:
            fila_minas.append("*")
    linea = "".join(fila_minas)
    minas_procesado.append(linea)
    fila_minas.clear()
print(minas)
print(minas_procesado)