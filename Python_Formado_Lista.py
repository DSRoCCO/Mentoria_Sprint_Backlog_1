"""listing_fruits function"""
from typing import List

def listing_fruits(list1: List):
    result = []
    for n in range(len(list1)):
        result.append(n+1)
        result.append(list1[n])

    return result

if __name__ == "__main__":

    #driver code
    print(listing_fruits(["Banana", "Strawberry", "Lemon"]) == [1, "Banana", 2, "Strawberry", 3, "Lemon"])
