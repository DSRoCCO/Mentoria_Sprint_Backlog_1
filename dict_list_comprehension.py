"""dict_list_comprehension function"""

def dict_list_comprehension(lista=None):
    result = []
    if lista is not None:
        [result.append(dict(zip(tupla[::2],tupla[1::2]))) for tupla in lista]

    return result
