"""this test must not be modified"""
class Person:
    def __init__(self, name = 'Robertina', job = 'Teacher'):
        self. name = name
        self. job = job

"""driver code"""
if __name__=="__main__":
    someone = Person()
    print(someone.name == 'Robertina')
    print(someone.job == 'Teacher')
    print('\n')
    manager = Person(job = 'Manager')
    print(manager.job == 'Manager')
