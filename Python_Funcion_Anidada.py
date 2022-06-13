#Función Anidada con Python
#Para este ejercicio hay que recordar las funciones anidadas y documentarse acerca de la funciones nativas de Python que pueden ayudarte en este ejercicio.
#Define la función anidada average que recibe una lista de calificaciones y calcula el promedio. El resultado de las comparaciones finales debe ser True.

def average(lista:list()):
    print(lista)
    ave= round(sum(lista)/len(lista),2)
    
    return "El promedio de la lista es: " + str(ave)

def uso_de(metodo: str):
    mensaje = " USO DE " + metodo.upper()+" "
    print(mensaje.center(50,"-"))
    
if __name__=='__main__':
    uso_de("Funciones Anidadas")
    print(average([2,4,2])=="El promedio de la lista es: 2.67")
    
    print(average([10,2,7,9,5])=="El promedio de la lista es: 6.6")
    
    