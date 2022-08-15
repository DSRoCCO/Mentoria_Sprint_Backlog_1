"""Iterative function"""
def Factorial_Iter(num):
    factorial = 1
    for n in range(1,num+1):
        factorial *= n
    return factorial

#"""Recursive function"""
def Factorial_Rec(num):
    if num == 0:
        return 1
    else:
        return num * Factorial_Rec(num-1)


#"""Iterative function"""
def Fibonacci_Iter(num):
    fibonacci = []
    if num <= 1:
        fibonacci.append(num)
    else:
        fibonacci=[0,1]
        for _ in range(2,num+1):
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[-1]

#"""Recursive function"""
def Fibonacci_Rec(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return Fibonacci_Rec(num-1) + Fibonacci_Rec(num-2)


if __name__ == '__main__':

    print("-"*10+"FACTORIAL ITERATIVO"+"-"*10)
    print(Factorial_Iter(0) == 1)
    print(Factorial_Iter(1) == 1)
    print(Factorial_Iter(5) == 120)
    print(Factorial_Iter(10) == 3628800)

    print("-"*10+"FACTORIAL RECURSIVIDAD"+"-"*10)
    print(Factorial_Rec(0) == 1)
    print(Factorial_Rec(1) == 1)
    print(Factorial_Rec(5) == 120)
    print(Factorial_Rec(10) == 3628800)

    print("-"*10+"FIBONACCI ITERATIVO"+"-"*10)
    print(Fibonacci_Iter(0) == 0)
    print(Fibonacci_Iter(1) == 1)
    print(Fibonacci_Iter(2) == 1)
    print(Fibonacci_Iter(20) == 6765)
    print(Fibonacci_Iter(50) == 12586269025)

    print("-"*10+"FIBONACCI RECURSIVIDAD"+"-"*10)
    print(Fibonacci_Rec(0) == 0)
    print(Fibonacci_Rec(1) == 1)
    print(Fibonacci_Rec(2) == 1)
    print(Fibonacci_Rec(7) == 13)
    print(Fibonacci_Rec(20) == 6765)
    print(Fibonacci_Rec(50) == 12586269025)

