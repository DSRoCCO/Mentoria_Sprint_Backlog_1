"""maximum difference function"""

def maximum_difference(list_of_numbers):
    return max(list_of_numbers) - min(list_of_numbers)

if __name__ == '__main__':

    #driver code
    print(maximum_difference([1, 2, 5, 0]) == 5)
    print(maximum_difference([1, 2, 5]) == 4)
