import unittest
import Python_Transformando_lista_diccionario_3

class Test_Transformacion_Lista_Diccionario(unittest.TestCase):
    def test_convert_list_to_dict(self):
        self.assertEqual(Python_Transformando_lista_diccionario_3.convert_list_to_dict([["computer", "Dell"], ["processor", "Intel"]]),{'computer': 'Dell', 'processor': 'Intel'})


if __name__ == '__main__':
    unittest.main()
