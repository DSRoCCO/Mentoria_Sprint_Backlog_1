"""dict_list_comprehension function"""

def dict_list_comprehension(lista):
    return [{tupla[i]:tupla[i+1] for tupla in lista for i in range(0,len(tupla),2)}]
