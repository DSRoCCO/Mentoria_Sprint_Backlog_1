
# Driver code

"""function to get fibonacci sequence"""

def get_fibonacci_seq(n):
    secuencia = []
    if n < 0:
        secuencia = "Incorrect input"
    for i in range(n+1):
        secuencia.append(fibonacci(i))

    return secuencia

"""function to get fibonacci for a number"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2)
    return n

if __name__=="__main__":

    #fibonacci sequence for -1
    print(get_fibonacci_seq(-1) == "Incorrect input")

    #fibonacci sequence for 1
    print(get_fibonacci_seq(1) == [0, 1])

    #fibonacci sequence for 5
    print(get_fibonacci_seq(5) == [0, 1, 1, 2, 3, 5])

    #fibonacci sequence for 10
    print(get_fibonacci_seq(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

