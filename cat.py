"""Bird class"""

class Cat:
    def __init__(self, name = None):
        name = self
        self.name = name

    def who_am_i(self):
        return self

    @classmethod
    def miau(cls):
        return "I'm going to Miau this time. Miau...!"

    @classmethod
    def doble_miau(cls):
        return "Miau... Miau"

"""driver code"""
if __name__=="__main__":

    # Let's create fido
    fido = Cat()
    print("1. ", fido.miau() == "I'm going to Miau this time. Miau...!")
    print("2. ", fido.who_am_i() == fido)

    # Let's create another fido
    new_fido = Cat()
    print("3. ", new_fido.who_am_i() == new_fido)

    #fido.doble_miau = make_a_miau  <- ?
    print("4. ", fido.doble_miau() == "Miau... Miau")

