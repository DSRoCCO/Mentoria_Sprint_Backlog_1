"""dog class"""
class Dog:
    def __init__(self, name, age, raza, vacunado):
        self.name = name
        self.age = age
        self.raza = raza
        self.vacunado = vacunado

"""people class"""
class People:
    def __init__(self, name, lastname, age, genero):
        self.name = name
        self.lastname= lastname
        self.age = age
        self.genero = genero


"""animal class"""
class Animal:
    def __init__(self, name, age, tipo, clas_alimentacion, clas_anatomia, clas_reproduccion, class_habitad ):
        self.name = name
        self.age = age
        self.tipo = tipo
        self.clas_alimentacion = clas_alimentacion
        self.clas_anatomia = clas_anatomia
        self.clas_reproduccion = clas_reproduccion
        self.clas_habitad = class_habitad

"""book class"""
class Book:
    def __init__(self, titulo, autor, edicion, anho):
        self.titulo = titulo
        self.autor= autor
        self.edicion = edicion
        self.anho = anho


if __name__=="__main__":

    #dog objects
    Perro_1 = Dog(name = "Firulas",
                    age = 1,
                    raza =  "Doberman",
                    vacunado = True)
    print(Perro_1)
    print(Perro_1.name)

    #people objects
    Persona_1 = People("Roger", "Cansaya", 33, "Masculino")
    print(Persona_1)
    print(Persona_1.name)

    #animal objects
    Animal_1 = Animal(name = "Claudio",
                    age = 1,
                    tipo = "Gallo",
                    clas_alimentacion = "Hervivoro",
                    clas_anatomia = "Vertebrado",
                    clas_reproduccion = "Oviparo",
                    class_habitad = "Terrestre")
    print(Animal_1)
    print(Animal_1.name)

    #book objects
    Book_1 = Book(titulo ="El camino del hombre superior",
                    autor = "Devid Deida",
                    edicion = "1era",
                    anho = 2020)
    print(Book_1)
    print(Book_1.titulo)
