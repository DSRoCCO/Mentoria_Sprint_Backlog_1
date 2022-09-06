
def modify_list(lista, exp_lambda):
    return [exp_lambda(value) for value in lista]

def modify_list2(lista, exp_lambda):
    return [round(exp_lambda(value),2) for value in lista]


# lambda expression
mod = lambda m, n: m % n

# divisor function
def divisor(num):
    return mod(num,2)

# divisible2 function
def divisible2(n):
    if mod(n,2) == 1:
        return 0
    else:
        return 1

# driver code
if __name__=="__main__":

### Ejercicio 1
    print("Ejercicio 1")
    numbers = [2,4,6,8]
    lmbda = lambda a : a * 2

    print(modify_list(numbers, lmbda) == [4, 8, 12, 16])

### Ejercicio 2
    print("Ejercicio 2")
    convert = lambda n: n + 273.15
    print(convert(27) == 300.15)

### Ejercicio 3
    print("Ejercicio 3")
    temps = [16, 20, 30, -30, 25]
    print(modify_list2(temps, convert)== [289.15, 293.15, 303.15, 243.15, 298.15])

### Ejercicio 4
    print("Ejercicio 4")
    print(divisor(10) == 0)

    print(divisible2(16) == 1)
    print(divisible2(3) == 0)
