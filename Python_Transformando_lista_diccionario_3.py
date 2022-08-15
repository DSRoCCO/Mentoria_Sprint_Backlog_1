"""convert_list_to_dict function goes here"""

def convert_list_to_dict(array):
    result = {}
    for n in range(len(array)):
        result [array[n][0]]=array[n][1]
    return result

