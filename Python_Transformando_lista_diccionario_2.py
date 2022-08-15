"""get_all_keys function goes here"""
def get_all_keys(*args):
    for arg in args:
        return [arg['name'],arg['age']]
