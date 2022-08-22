import unittest
from find_upper_OBS import *


class FindUpperTests(unittest.TestCase):

	def test_find_upper_for_person1_and_person1(self):
		person1 = {"name": "candy", "last_name": "Feder", "age": 34}
		person2 = {"name": "Manuel", "last_name": "martínes", "age": 21}
		expected_dict = {'F': 'Feder'}
		self.assertEqual(find_upper(person1, person2), expected_dict)

	def test_find_upper_for_person3_and_person4(self):
		person3 = {"name": "moni", "last_name": "Perales", "age": 22}
		person4 = {"name": "lourdes", "last_name": "Montoya", "age": 27}
		expected_dict = {'P': 'Perales', 'M': 'Montoya'}
		self.assertEqual(find_upper(person3, person4), expected_dict)

if __name__=="__main__":
    unittest.main()
