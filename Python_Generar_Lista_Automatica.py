"""random_list function"""
import random
def random_list(alumnis, n, min_value, max_value):
    ## con List Comprehension
    result = [[alum ,[random.randint(min_value, max_value) for _ in range(n)]] for alum in alumnis]
    return result

def random_list2(alumnis, n, min_value, max_value):
    ## con for loop
    notas = []
    calififaciones = []

    for alum in alumnis:
        notas.clear()
        for _ in range(n):
            notas.append(random.randint(min_value, max_value))
        calififaciones.append([alum, notas])


    return calififaciones


if __name__ == '__main__':

#driver code
### Con List comprehension
#"""Ejemplo 1"""
    print(random_list(["Robert", "Charlis", "Marco", "Pepe", "Angi"], 7, 5, 10))
#[['Robert', [5, 8, 5, 7, 5, 9, 8]], ['Charlis', [5, 8, 10, 8, 7, 7, 10]], ['Marco', [9, 5, 10, 8, 8, 5, 8]], ['Pepe', [6, 7, 5, 7, 8, 6, 8]], ['Angi', [7, 6, 7, 8, 9, 7, 7]]]


#"""Ejemplo 2"""
    print(random_list(["Faby", "Moni", "Stefani", "Herni"], 5, 1, 10))
#[['Faby', [8, 10, 8, 1, 9]], ['Moni', [7, 10, 6, 6, 8]], ['Stefani', [1, 8, 8, 10, 5]], ['Herni', [9, 8, 9, 7, 5]]]



### Con for loop

    print(random_list2(["Robert", "Charlis", "Marco", "Pepe", "Angi"], 7, 5, 10))
    print(random_list2(["Faby", "Moni", "Stefani", "Herni"], 5, 1, 10))
