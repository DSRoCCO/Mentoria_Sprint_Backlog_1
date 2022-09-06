"""second_grade function"""

from itertools import count


def second_grade():
    """Obtiene la segunda calificación más baja de la lista."""
    notas = []
    #se obtienen las entradas del usuario
    n_entradas = int(input("Cuantas notas desea ingresar: "))
    for n in range(n_entradas):
        nombre = input("Ingrese Nombre del Alumno: ")
        nota = float(input("Ingrese nota del Alumno: "))
        notas.append([nombre,nota])
    print(notas)

    """Obtiene la mínima calificación de la lista."""
    #se obtiene la mínima calificación
    def minimum(array):
        result = sorted(array, key = lambda x: x[1])                    #ordenando

    #se obtienen los elementos con calificaciones diferentes a la mínima
        result = list(filter(lambda x: x[1] != result[0][1], result))   #Eliminando la nota mas baja


    #se obtienen los segundas calificaciones mínimas
        result = list(filter(lambda x: x[1] == result[0][1], result))   # Capturando la 2da nota mas baja


    #se retorna la lista de nombres ordenada alfabéticamente
        result = sorted(result, key = lambda x: x[0])
        result = [val[0] for val in result]
        return result

    return minimum(notas)

