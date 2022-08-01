"""maximum difference function"""

def maximum_difference(list_of_numbers):
    mini, maxi = [], []
    mini.append(list_of_numbers[0])
    maxi.append(list_of_numbers[0])
    [mini.append(number) for number in list_of_numbers if number < mini[-1]]
    [maxi.append(number) for number in list_of_numbers if number > maxi[-1]]
    return maxi[-1] - mini[-1]

if __name__ == '__main__':

    #driver code
    print(maximum_difference([1, 2, 5, 0]) == 5)
    print(maximum_difference([1, 2, 5]) == 4)
