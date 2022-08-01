import unittest
import Python_Detectando_Mayuscula

person1 = {"name": "candy", "last_name": "Feder", "age": 34}
person2 = {"name": "Manuel", "last_name": "martínes", "age": 21}

class TestMayuscula(unittest.TestCase):
    def test_find_upper(self):
        self.assertEqual(Python_Detectando_Mayuscula.find_upper(person1, person2),{'F': 'Feder'})

if __name__ == '__main__':
    unittest.main()
