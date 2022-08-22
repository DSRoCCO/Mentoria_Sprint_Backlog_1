import unittest
from nested_list_to_dict import *


class NestedListToDictTests(unittest.TestCase):

	def test_nested_list_to_dict_for_one_nested_list(self):
		data = [[['firstName', 'Oscar'], ['lastName', 'Majik'], ['age', 56], ['country', 'Mexico']]]
		expected_list_with_dict = [{'firstName': 'Oscar', 'lastName': 'Majik', 'age': 56, 'country': 'Mexico'}]
		self.assertEqual(nested_list_to_dict(data), expected_list_with_dict)

	def test_nested_list_to_dict_for_two_nested_list(self):
		data = [[['firstName', 'Oscar'], ['lastName', 'Majik'], ['age', 56], ['country', 'Mexico']], [['firstName', 'Pamel'], ['lastName', 'Herkan'], ['age', 26], ['country', 'Polonia']]]
		expected_list_with_dict = [{"firstName": 'Oscar', "lastName": 'Majik', "age": 56, "country": 'Mexico'}, {"firstName": 'Pamel', "lastName": 'Herkan', "age": 26, "country": 'Polonia'}]
		self.assertEqual(nested_list_to_dict(data), expected_list_with_dict)

	def test_nested_list_to_dict_for_two_nested_list_dif_len(self):
		data = [[['firstName', 'Oscar'], ['lastName', 'Majik'], ['age', 56]], [['firstName', 'Pamel'], ['lastName', 'Herkan'], ['age', 26], ['country', 'Polonia']]]
		expected_list_with_dict = [{'firstName': 'Oscar', 'lastName': 'Majik', 'age': 56}, {'firstName': 'Pamel', 'lastName': 'Herkan', 'age': 26, 'country': 'Polonia'}]
		self.assertEqual(nested_list_to_dict(data), expected_list_with_dict)

	def test_nested_list_to_dict_for_empty_argument(self):
		expected_list_with_dict = []
		self.assertEqual(nested_list_to_dict(), expected_list_with_dict)

if __name__=="__main__":
    unittest.main()
