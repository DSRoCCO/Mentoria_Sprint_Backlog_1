import unittest
from get_all_keys import *


class GetAllKeysTests(unittest.TestCase):

	def test_get_all_keys_for_person1_and_person2_dict(self):
		person1 = {"name": "Fernando", "age": 34}
		person2 = {"name": "Morelia", "height": 1.70}
		expected_list = ['name', 'age', 'height']
		self.assertEqual(get_all_keys(person1, person2), expected_list)

	def test_get_all_keys_for_person2_dict(self):
		person2 = {"name": "Morelia", "height": 1.70}
		expected_list = ['name', 'height']
		self.assertEqual(get_all_keys(person2), expected_list)

	def test_get_all_keys_for_person1_and_person2_and_object1(self):
		person1 = {"name": "Fernando", "age": 34}
		person2 = {"name": "Morelia", "height": 1.70}
		object1 = {"color": "blue", "quantity": 50}
		expected_list = ['name', 'age', 'height', 'color', 'quantity']
		self.assertEqual(get_all_keys(person1, person2, object1), expected_list)


if __name__=="__main__":
    unittest.main()
