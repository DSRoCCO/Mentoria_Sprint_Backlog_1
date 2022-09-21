
"""Driver class"""

class Driver:

    def __init__(self, first, last, occupation):
        self.first = first
        self.last = last
        self.occupation = occupation

"""Driver Passenger"""

class Passenger:
    """
    def __init__(self, first = None, last=None, email = None, rides_taken = 0):
        self.first = first
        self.last = last
        self.email = email
        self.rides_taken = rides_taken
    """
    def __init__(self, first = "Carlos", last="Standley", email = "carlos.stand@mailimax.com", rides_taken = 0):
        self.first = first
        self.last = last
        self.email = email
        self.rides_taken = rides_taken

"""driver code"""

if __name__=="__main__":

    gary_white = Driver('Gary','White','Astronaut')

    print(gary_white.first == "Gary")
    print(gary_white.last == "White")
    print(gary_white.occupation == "Astronaut")

    carlos = Passenger('Carlos','Standley','carlos.stand@mailimax.com')

    print(carlos.first == "Carlos")
    print(carlos.last == "Standley")
    print(carlos.email == "carlos.stand@mailimax.com")
    print(carlos.rides_taken == 0)

    moyu = Passenger('Yakohama','Moyu','yaku.yu@mailimax.com')
    print(moyu.first == "Yakohama")
    print(moyu.last == "Moyu")
    print(moyu.email == "yaku.yu@mailimax.com")
    print(moyu.rides_taken == 0)

    carlos = Passenger(rides_taken = 7)
    print(carlos.first == "Carlos")
    print(carlos.last == "Standley")
    print(carlos.email == "carlos.stand@mailimax.com")
    print(carlos.rides_taken == 7)
