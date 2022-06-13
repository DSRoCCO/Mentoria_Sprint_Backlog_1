#Ejercicio - Función vacía en Python
#Define la función hello que no realiza ninguna acción.

from inspect import _void

def uso_de(metodo: str):
    mensaje = " USO DE " + metodo.upper()+" "
    print(mensaje.center(50,"-"))

def hello(): # funcion void
    pass

def move(speed, time):
    distancia = speed * time
    return "El carro avanza: "+ str(distancia) + " metros"

if __name__ == '__main__':
    
    uso_de("Funcion Void")
    print(hello() == None)
    
    uso_de("Funcion Move")
    print(move(2,3) == "El carro avanza: 6 metros")