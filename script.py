"""
script.py: script module, where it can be instances created and evaluated.
"""
from ride import Ride
from driver import Driver
from passenger import Passenger

def main():
    gussi = Passenger(None)
    serena = Passenger(None)

    taxi = Driver(None)

    ride_to_mexico = Ride(None)
    ride_home = Ride(None)

    """driver code"""

    print(isinstance(gussi, Passenger))
    print(isinstance(serena, Passenger))
    print(isinstance(taxi, Driver))
    print(isinstance(ride_to_mexico, Ride))
    print(isinstance(ride_home, Ride))

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()

