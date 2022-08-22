"""nested_list_to_dict function"""

def nested_list_to_dict(lista=None):
    result = []
    if lista is not None:
        [result.append(dict(arrays)) for arrays in lista]

    return result
