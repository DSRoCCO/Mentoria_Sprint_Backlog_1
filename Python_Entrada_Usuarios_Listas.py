

def user_list():
    num = int(input("Ingrese la cantidad de comandos a ingresar: "))
    list1 = []
    while num > 0:
        comando = input("Ingrese comando y valores separados por un espacio: ")
        comando = comando.split(" ")

        if comando[0] == "insert":
            list1.insert(int(comando[1]),int(comando[2]))
            num -= 1
        elif comando[0] == "remove":
            list1.remove(int(comando[1]))
            num -= 1
        elif comando[0] == "append":
            list1.append(int(comando[1]))
            num -= 1
        elif comando[0] == "reverse" or comando[0] == "r":
            list1.reverse()
            num -= 1
        elif comando[0] == "pop" or comando[0] == "p":
            list1.pop()
            num -= 1
        elif comando[0] == "sort" or comando[0] == "s":
            list1.sort()
            num -= 1
        else:
            print(" Ingrese Comando Nuevamente")
    return list1

if __name__ == "__main__":

    #driver code
    """Ejemplo 1 de entradas de usuario"""
    """
    5
    insert 0 7
    insert 1 8
    insert 2 9
    insert 3 3
    insert 0 15
    """
    print(user_list() == [15, 7, 8, 9, 3])
    # True

    """Ejemplo 2 de entradas de usuario"""
    """
    11
    insert 0 7
    insert 1 8
    insert 2 9
    insert 3 3
    insert 0 15
    remove 9
    append 90
    append 100
    remove 8
    append 20
    sort
    """
    print(user_list() == [3, 7, 15, 20, 90, 100])
    # True

    """Ejemplo 3 de entradas de usuario"""
    """
    17
    insert 0 7
    insert 1 8
    insert 2 9
    insert 3 3
    insert 0 15
    remove 9
    append 9
    append 90
    append 100
    remove 8
    append 20
    sort
    pop
    reverse
    pop
    reverse
    insert 0 47
    """
    print(user_list() == [47, 7, 9, 15, 20, 90])
    # True
