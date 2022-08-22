import unittest
from convert_list_to_dict import *


class ConvertListToDictTests(unittest.TestCase):

	def test_convert_list_to_dict_for_two_nested_list(self):
		input_nested_list = [["computer", "Dell"], ["processor", "Intel"]]
		expected_dict = {'computer': 'Dell', 'processor': 'Intel'}
		self.assertEqual(convert_list_to_dict(input_nested_list), expected_dict)

	def test_convert_list_to_dict_for_one_nested_list(self):
		input_nested_list = [["celular", "iphone"]]
		expected_dict = {'celular': 'iphone'}
		self.assertEqual(convert_list_to_dict(input_nested_list), expected_dict)

	def test_convert_list_to_dict_for_empty_argument(self):
		expected_dict = {}
		self.assertEqual(convert_list_to_dict(), expected_dict)

if __name__=="__main__":
    unittest.main()
