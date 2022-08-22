import unittest
from dict_list_comprehension import *


class DictListComprehensionTests(unittest.TestCase):

	def test_dict_list_comprehension_for_list_with_two_tuples(self):
		input_list = [(1,'alex',2,'beatriz',3,'carla'), (4,'daniel',5,'ernesto',6,'fede')]
		expected_list_with_dict = [{1: 'alex', 2: 'beatriz', 3: 'carla'}, {4: 'daniel', 5: 'ernesto', 6: 'fede'}]
		self.assertEqual(dict_list_comprehension(input_list), expected_list_with_dict)

	def test_dict_list_comprehension_for_list_with_one_tuple(self):
		input_list = [(1,'alex',2,'beatriz',3,'carla')]
		expected_list_with_dict = [{1: 'alex', 2: 'beatriz', 3: 'carla'}]
		self.assertEqual(dict_list_comprehension(input_list), expected_list_with_dict)

	def test_dict_list_comprehension_for_list_with_two_tuples_dif_len(self):
		input_list = [(1,'alex',2,'beatriz',3,'carla'), (4,'daniel')]
		expected_list_with_dict = [{1: 'alex', 2: 'beatriz', 3: 'carla'}, {4: 'daniel'}]
		self.assertEqual(dict_list_comprehension(input_list), expected_list_with_dict)

if __name__=="__main__":
    unittest.main()
