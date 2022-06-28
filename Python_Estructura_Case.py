#=> "You are Third"
#"""python functions"""

#one function
def one():
        return "You are One"

#second function
def second():
        return "You are Second"

#third function
def third():
        return "You are Third"

#default function
def default():
        return "You are the best"

#numbers_to_ranges function
def numbers_to_ranges(speed):
    ranges=[list(range(0,21)),list(range(21,31)),list(range(31,41))]
#switch_example function
    def switch_example(speed, ranges):
        if speed in ranges[0]:
            number = 0
        elif speed in ranges[1]:
            number = 1
        elif speed in ranges[2]:
            number = 2
        else:
            number = 3
        switch= {0:one(), 1:second(), 2:third(), 3:default()}
        return switch.get(number,"Invalid")

    func = switch_example(speed, ranges)
    return func

if __name__ == '__main__':
    #driver code

    #switch o case con número 37
    print(numbers_to_ranges(37) == "You are Third")
    #switch o case con número 10
    print(numbers_to_ranges(10) == "You are One")
    #switch o case con número 25
    print(numbers_to_ranges(25) == "You are Second")
    #switch o case con número 41
    print(numbers_to_ranges(41) == "You are the best")

