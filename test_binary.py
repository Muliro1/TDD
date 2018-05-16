#the following are testcases for the binary search algorithm
import unittest

from search import binary_search

class TestBinary(unittest.TestCase):

	def test_found(self):

		self.assertEqual(binary_search(1, [1,2,3,4]), True)

		self.assertEqual(binary_search(1, [2,3,4]), False)

	def test_input(self):

		self.assertRaises(TypeError, binary_search, 'string')

		

		




if __name__ == '__main__':

	unittest.main()