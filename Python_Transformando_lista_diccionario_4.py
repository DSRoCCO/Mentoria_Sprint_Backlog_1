"""nested_list_to_dict function"""

def nested_list_to_dict(lista):
    return [{array[0]:array[1] for arrays in lista for array in arrays}]


