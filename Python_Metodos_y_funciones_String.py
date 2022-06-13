# Métodos y funciones de string en Python
#Python tiene métodos que pueden ser aplicados para desarrollar una tarea sobre un string, 
# asimismo tiene también funciones que pueden tomar como parámetro un string y desarrollar cierta tarea.
#Algunos métodos y funciones de string

#count
#index
#isdecimal
#center
#capitalize
#find
#len
#lower
#upper
#strip
#split
#startswith
#max
#min

def uso_de(metodo: str):
    mensaje = " USO DE " + metodo.upper()+" "
    print(mensaje.center(50,"-"))
    
if __name__ == '__main__':
    
    hola = "bienvenido"
    hola2 = "al curso"
    hola3 = "este sabado"
    string_result = hola + " "*4 + hola2+" "*3
    uso_de("upper")
    print(string_result.upper() =='BIENVENIDO    AL CURSO   ')

    uso_de("capitalize")
    uso_de("strip")
    print(string_result.strip().capitalize() =='Bienvenido    al curso')
    
    uso_de("len")
    print(len(string_result)==25)
    
    uso_de("count")
    print(string_result.count("e")==2)
    
    string_result = hola + " "*4 + hola3
    uso_de("Split")
    print(string_result.split()==['bienvenido','este','sabado'])
    
    variable = "ana"
    uso_de("len")
    print(len(variable)==3)

