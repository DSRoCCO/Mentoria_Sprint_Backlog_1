import unittest
from unittest.mock import patch
from second_grade import *


class SecondGradeTests(unittest.TestCase):

	def test_second_grade_for_user_example_one(self):
		user_input = ["3", "Robert", "23.5", "Karla", "23.5", "Rodrigo", "23"]
		expected_list = ['Karla', 'Robert']
		with patch('builtins.input', side_effect=user_input):
		    self.assertEqual(second_grade(), expected_list)

	def test_second_grade_for_user_example_two(self):
		user_input = ["5", "Faby", "35.6", "Gaby", "35", "Lourdes", "35.6", "Magy", "47", "Pepe", "50"]
		expected_list = ['Faby', 'Lourdes']
		with patch('builtins.input', side_effect=user_input):
		    self.assertEqual(second_grade(), expected_list)

	def test_second_grade_for_user_example_three(self):
		user_input = ["3", "Robert", "23.5", "Karla", "50.4", "Rodrigo", "23"]
		expected_list = ['Robert']
		with patch('builtins.input', side_effect=user_input):
		    self.assertEqual(second_grade(), expected_list)


if __name__=="__main__":
    unittest.main()
