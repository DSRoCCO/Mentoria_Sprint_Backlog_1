import unittest
from list_lambda import list_to_lambda

class LambdaTest(unittest.TestCase):
	def test_range_10(self):
		expected = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
		self.assertEqual(list_to_lambda(range(10)), expected)

	def test_range_6(self):
		expected = [4, 5, 6, 7, 8, 9]
		self.assertEqual(list_to_lambda(range(6)), expected)

	def test_range_12(self):
		expected = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
		self.assertEqual(list_to_lambda(range(12)), expected)

	def test_range_0(self):
		expected = "Invalid Operation"
		self.assertEqual(list_to_lambda(range(0)), expected)


if __name__=="__main__":
	unittest.main(verbosity=2)
