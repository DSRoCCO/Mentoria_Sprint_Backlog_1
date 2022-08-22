"""get_all_keys function goes here"""
def get_all_keys(*args):
    result = []
    for arg in args:
        for key in arg.keys():
            if key not in result:
                result.append(key)
    return result
