import unittest
import Python_Transformando_lista_diccionario_2

person1 = {"name": "Fernando", "age": 34}
person2 = {"name": "Morelia", "age": 54}

class Test_Transformacion_Lista_Diccionario(unittest.TestCase):
    def test_get_all_keys(self):
        self.assertEqual(Python_Transformando_lista_diccionario_2.get_all_keys(person1,person2),['Fernando', 34])


if __name__ == '__main__':
    unittest.main()
