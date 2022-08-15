import unittest
import Python_List_compreh_dict_compreh_tuplas

inn = [(1,'alex',2,'beatriz',3,'carla')]

class Test_Transformacion_Lista_Diccionario(unittest.TestCase):
    def test_convert_list_to_dict(self):
        self.assertEqual(Python_List_compreh_dict_compreh_tuplas.dict_list_comprehension(inn),[{1: 'alex', 2: 'beatriz', 3: 'carla'}])


if __name__ == '__main__':
    unittest.main()

