import unittest
import Python_Transformando_lista_diccionario


class TestMayuscula(unittest.TestCase):
    def test_get_first_and_last(self):
        self.assertEqual(Python_Transformando_lista_diccionario.get_first_and_last(["oro", "arroz", "molido"]),{'oro': 'molido'})

if __name__ == '__main__':
    unittest.main()
