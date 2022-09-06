#code goes here

def list_to_lambda(rango):
    if rango == range(0):
        return "Invalid Operation"
    else:
        return list(map(lambda x: x+2**2, rango))
