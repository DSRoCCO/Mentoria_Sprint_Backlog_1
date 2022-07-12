from typing import List

"""function to return the first n elements of the list"""

def first_n(list1: List,n):
    return list1[:n]


"""function to drop the first n elements of the list and return the rest"""

def drop_n(list1: List,n):
    list1 = list1[n:]
    return list1


"""function to add 'element' to the end of the list"""
def end_lis_add(list1: List,n):
    list1.append(n)
    return list1


"""function to add 'element' to the beginning of the list"""
def begin_lis_add(list1: List,n):
    list1.insert(0,n)
    return list1


"""function to add 'element' at position 'index' to the list"""
def index_lis_add(list1: List,n,m):
    list1.insert(n,m)
    return list1

"""function to add any two elements to the list at the index"""

def index_lis_multiple_add(list1: List,n,*argv):
    for arg in argv:
        list1.insert(n,arg)
        n += 1
    return list1

"""function to delete the element from the end of the list and return the deleted element"""
def end_lis_delete(list1: List):
    return list1.pop()


"""function to delete the element at the beginning of the list"""
def start_lis_delete(list1:List):
    list1.pop(0)
    return list1


"""function to delete the element at the position 'index'"""
def delete_at_lis(list1:List, n):
    list1.pop(n)
    return list1

"""function to delete the element of the list where element = val"""
def remove_val_lis(list1: List, n):
    list1.remove(n)
    return list1


if __name__ == "__main__":

    #driver code
    print("function to return the first n elements of the list")
    print(first_n([1, 4, 3, 6, 5], 3) == [1, 4, 3])
    print("function to drop the first n elements of the list and return the rest")
    print(drop_n([1, 4, 3, 6, 5], 3) == [6, 5])
    print("function to add 'element' to the end of the list")
    print(end_lis_add([1, 4, 3, 6, 5], 20) == [1, 4, 3, 6, 5, 20])
    print("function to add \'element\' to the beginning of the list")
    print(begin_lis_add([1, 4, 3, 6, 5], 34) == [34, 1, 4, 3, 6, 5])
    print("function to add 'element' at position 'index' to the list")
    print(index_lis_add([1, 4, 3, 6, 5], 2, 100) == [1, 4, 100, 3, 6, 5])
    print("function to add any two elements to the list at the index")
    print(index_lis_multiple_add([1, 4, 3, 6, 5], 3, 34, 23) == [1, 4, 3, 34, 23, 6, 5])
    print("function to delete the element from the end of the list and return the deleted element")
    print(end_lis_delete([1, 4, 3, 6, 5]) == 5)
    print("function to delete the element at the beginning of the list")
    print(start_lis_delete([1, 4, 3, 6, 5]) == [4, 3, 6, 5])
    print("function to delete the element at the position \'index\'")
    print(delete_at_lis([1, 4, 3, 6, 5], 2) == [1, 4, 6, 5])
    print("function to delete the element of the list where element = val")
    print(remove_val_lis([1, 4, 3, 6, 5], 6) == [1, 4, 3, 5])
