import unittest
import Python_Transformando_lista_diccionario_4

a =[
        [
            ['firstName', 'Oscar'], ['lastName', 'Majik'], ['age', 56], ['country', 'Mexico']
        ]
    ]

class Test_Transformacion_Lista_Diccionario(unittest.TestCase):
    def test_convert_list_to_dict(self):
        self.assertEqual(Python_Transformando_lista_diccionario_4.nested_list_to_dict(a),[{'firstName': 'Oscar', 'lastName': 'Majik', 'age': 56, 'country': 'Mexico'}])


if __name__ == '__main__':
    unittest.main()
