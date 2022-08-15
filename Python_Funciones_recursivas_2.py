"""Recursive function"""

def mysum(numbers):
    #print("first numbers", numbers)
    """recursive function to add numbers of list"""
    # when not numbers
    if not numbers: # no hay mas
        return 0

    # when index '0' of numbers is a list
    elif type(numbers) is list:
        return (mysum(numbers[0]) + mysum(numbers[1:]))

    # when index '0' of numbers is not a list
    elif type(numbers) is not list:
        return numbers


    """driver code"""

if __name__ == '__main__':

    print(mysum([10,[21,32,43],54,[63,[72,81],90]]) == 466)
    print(mysum([10,[21,[32,43]],[54,[63,[72,81]],90]]) == 466)
    print(mysum([10,[21,[32,43]],54,[63,[72,81,[1,1,[1,1]]],90]]) == 470)
