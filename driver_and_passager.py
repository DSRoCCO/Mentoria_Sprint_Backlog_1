
"""Driver class"""
from typing import List


list_of_drivers = []
list_of_passengers = []

class Driver:

    def __init__(self, name=None, miles_driven= None, rating = None):
        self.name = name
        self.miles_driven = miles_driven
        self.rating = rating


"""Driver Passenger"""

class Passenger:

    def __init__(self, name= None):
        self.name = name

# Define the NewDriver class
class NewDriver:

    def __init__(self, name = "name", car_make = "car_make", car_model = "car_model", age = "age", passengers: List = []):
        self.name = name
        self.car_make = car_make
        self.car_model = car_model
        self.age = age
        self.passengers = passengers

    def passenger_names(self):
        return [obj.name for obj in self.passengers]


"""functions"""

# define find_driver_by_name function
def find_driver_by_name(name_2):
    if  [obj for obj in list_of_drivers if obj.name == name_2] == []:
        return "Sorry, we couldn't find a driver with the name, " + name_2.capitalize()+"! :("
    else:
        return [obj for obj in list_of_drivers if obj.name == name_2][0]

# Define your function here
def name_starts_with(lista, letra):
    return [obj for obj in lista if obj.name.startswith(letra)]


# driver code
def sort_lists_by_name(list):
    return sorted(name_starts_with(list, 'a'), key=lambda driver: driver.name)

# Write your function here that returns the driver with the highest rating
def highest_rated_driver(lista):
    drivers = {obj:obj.rating for obj in lista}
    highest = max(drivers.items(), key = lambda x: x[1]) #maximo rating y driver
    return highest[0]


if __name__=="__main__":

    # Assign a driver instance
    driver= Driver()
    # Give the driver instance object 'miles_driven' of 100000
    driver.miles_driven = 100000

    # Assign a passenger instance
    passenger= Passenger()
    # Give the passenger instance object a 'rating' of 4.9
    passenger.rating = 4.9

    print(isinstance(driver, Driver) == True)
    print(isinstance(passenger, Passenger) == True)
    print(passenger.rating == 4.9)
    print(driver.miles_driven == 100000)

    list_of_drivers.clear()
    # Create drivers with relevant attributes
    alex_driver = Driver(name = 'alex', rating = 9.0)
    michelle_driver = Driver(name = 'michelle', rating = 8.0)
    jake_driver = Driver(name = 'jake', rating = 9.7)
    ashleigh_driver = Driver(name = 'ashleigh', rating = 8.75)
    list_of_drivers = [alex_driver, michelle_driver, jake_driver, ashleigh_driver]

    # driver code
    print('alex_driver is Driver class instance?:    ', isinstance(alex_driver, Driver) == True)
    print('alex_driver has name?:                    ', hasattr(alex_driver, 'name'))
    print('alex_driver name is alex?:                ', True if alex_driver.name == "alex" else False if hasattr(alex_driver, 'name') else False)
    print('alex_driver has rating?:                  ', hasattr(alex_driver, 'rating'))
    print('alex_driver rating is 9.0?:               ', True if alex_driver.rating == 9.0 else False if hasattr(alex_driver, 'rating') else False)
    print("-" * 5)
    print('michelle_driver is Driver class instance?:', isinstance(michelle_driver, Driver) == True)
    print('michelle_driver has name?:                ', hasattr(michelle_driver, 'name'))
    print('michelle_driver name is michelle?:        ', True if michelle_driver.name == "michelle" else False if hasattr(michelle_driver, 'name') else False)
    print('michelle_driver has rating?:              ', hasattr(michelle_driver, 'rating'))
    print('michelle_driver rating is 8.0?:           ', True if michelle_driver.rating == 8.0 else False if hasattr(michelle_driver, 'rating') else False)
    print("-" * 5)
    print('jake_driver is Driver class instance?:    ', isinstance(jake_driver, Driver) == True)
    print('jake_driver has name?:                    ', hasattr(jake_driver, 'name'))
    print('jake_driver name is jake?:                ', True if jake_driver.name == "jake" else False if hasattr(jake_driver, 'jake') else False)
    print('jake_driver has rating?:                  ', hasattr(jake_driver, 'rating'))
    print('jake_driver rating is 9.7?:               ', True if jake_driver.rating == 9.7 else False if hasattr(jake_driver, 'rating') else False)
    print("-" * 5)
    print('ashleigh_driver is Driver class instance?:', isinstance(ashleigh_driver, Driver) == True)
    print('ashleigh_driver has name?:                ', hasattr(ashleigh_driver, 'name'))
    print('ashleigh_driver name is ashleigh?:        ', True if ashleigh_driver.name == "ashleigh" else False if hasattr(ashleigh_driver, 'ashleigh') else False)
    print('ashleigh_driver has rating?:              ', hasattr(ashleigh_driver, 'rating'))
    print('ashleigh_driver rating is 8.75?:          ', True if ashleigh_driver.rating == 8.75 else False if hasattr(ashleigh_driver, 'rating') else False)
    print("-" * 5)
    print('list_of_drivers is lenght 4?:             ', (len(list_of_drivers) if type(list_of_drivers) == list else False) == 4)

    # Find "jake"
    print('Encontramos a jake:                       ', find_driver_by_name('jake') == jake_driver)

    # Find "michelle"
    print('Encontramos a michelle:                    ', find_driver_by_name('michelle') == michelle_driver)

    # Find "allison"
    print('Encontramos a alisson:                     ', find_driver_by_name('allison') == "Sorry, we couldn't find a driver with the name, Allison! :(")

    # Find Charly
    print('Encontramos a Charly:                      ', find_driver_by_name('Charly') == "Sorry, we couldn't find a driver with the name, Charly! :(")


   # driver code
    print(sort_lists_by_name(name_starts_with(list_of_drivers, 'a')) == [alex_driver, ashleigh_driver])
    print(sort_lists_by_name(list_of_drivers)[1].name == 'ashleigh')
    print(name_starts_with(list_of_drivers, 'al') == [alex_driver])
    print(name_starts_with(list_of_drivers, 'az') == [])


    # driver code
    def create_mory_driver_instance():
        mory_driver = Driver()
        mory_driver.name = "mory"
        mory_driver.rating = 10.0
        return mory_driver


    mory = create_mory_driver_instance()
    list_of_drivers.append(mory)
    print(highest_rated_driver(list_of_drivers) is mory)

    ### Instance Method
    # Passengers
    alex_passenger = Passenger(name = 'alex')
    michelle_passenger = Passenger(name = 'michelle')
    jake_passenger = Passenger(name = 'jake')
    ashleigh_passenger = Passenger(name = 'ashleigh')
    list_of_passengers = [alex_passenger, michelle_passenger, jake_passenger, ashleigh_passenger]

    # driver code
    print('alex_passenger is Passenger class instance?:    ', isinstance(alex_passenger, Passenger) == True)
    print('alex_passenger has name?:                       ', hasattr(alex_passenger, 'name'))

    print('michelle_passenger is Passenger class instance?:', isinstance(michelle_passenger, Passenger) == True)
    print('michelle_passenger has name?:                   ', hasattr(michelle_passenger, 'name'))

    print('jake_passenger is Passenger class instance?:    ', isinstance(jake_passenger, Passenger) == True)
    print('jake_passenger has name?:                       ', hasattr(jake_passenger, 'name'))

    print('ashleigh_passenger is Passenger class instance?:', isinstance(ashleigh_passenger, Passenger) == True)
    print('ashleigh_passenger has name?:                   ', hasattr(ashleigh_passenger, 'name'))

    print('list_of_passengers is lenght 4?:                ', (len(list_of_passengers) if type(list_of_passengers) == list else False) == 4)


    # Instantiate a NewDriver class object
    best_driver = NewDriver()

    # driver code
    print(hasattr(best_driver, "name"))
    print(hasattr(best_driver, "car_make"))
    print(hasattr(best_driver, "car_model"))
    print(hasattr(best_driver, "age"))
    print(hasattr(best_driver, "passengers"))


    # Add the name attribute and assign it 'Garol'
    best_driver.name = "Garol"

    # Add the car_make attribute and assign it 'toyota'
    best_driver.car_make = "toyota"

    # Add the car_model attribute and assign it 'camry'
    best_driver.car_model = "camry"

    # Add the age attribute and assign it 30
    best_driver.age = 30

    # Add the passengers attribute and assign it to list_of_passengers
    best_driver.passengers = list_of_passengers


    #driver code
    print("\n")
    print(type(best_driver.name) == str)
    print(type(best_driver.car_make) == str)
    print(type(best_driver.car_model) == str)
    print(type(best_driver.age) == int)
    print(len(best_driver.passengers) == 4)

    # Find the names of the passengers with passenger_names()
    names_of_passengers = best_driver.passenger_names()

    #print(names_of_passengers)
    print(best_driver.passenger_names())

    # driver code
    print(names_of_passengers == ['alex', 'michelle', 'jake', 'ashleigh'])
