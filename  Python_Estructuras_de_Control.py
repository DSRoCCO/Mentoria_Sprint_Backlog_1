
"""even_odd function"""
#driver code
#print(even_odd([3, 1, 5, 6, 8, 10, 23, 25, 23]) == ['odd', 'odd', 'odd', 'even', 'even', 'even', 'odd', 'odd', 'odd'])
#print(even_odd([12, -4, -23, 0]) == ['even', 'even', 'odd', 'even'])

def even_odd(lista: list()):
    return  ["even" if abs(n)%2 == 0 else "odd" for n in lista]

if __name__ == '__main__':
    print(even_odd([3, 1, 5, 6, 8, 10, 23, 25, 23]) == ['odd', 'odd', 'odd', 'even', 'even', 'even', 'odd', 'odd', 'odd'])
    print(even_odd([12, -4, -23, 0]) == ['even', 'even', 'odd', 'even'])
