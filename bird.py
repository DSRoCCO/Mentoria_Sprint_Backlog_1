"""Bird class"""

class Bird:
    def __init__(self, name):
        self.name = name
        self.height = 0

    def jump(self):
        return "Saltando..."

    def flying(self, height_n = 0):
        self.height += height_n
        return "Volando "+ str(self.height) +" mts..."

    @classmethod
    def who_am_i(cls):
        return "Soy un pájaro"


