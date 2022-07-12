"""several_times function"""

from typing import List

def several_times(list1:List, list2:List, n_times):

    for n in range(n_times):
        list1.append(list2)
    return list1

if __name__ == "__main__":

    #driver code
    print(several_times(['f', 'g', 'h'], ['i', 'j', 'k'], 2) == ['f', 'g', 'h', ['i', 'j', 'k'], ['i', 'j', 'k']])
    print(several_times(['libreta', 'cuaderno'], ['hojas'], 4) == ['libreta', 'cuaderno', ['hojas'], ['hojas'], ['hojas'], ['hojas']])

