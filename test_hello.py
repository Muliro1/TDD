import unittest
from hello__ import hello_, counter

class TestHello(unittest.TestCase):
	def test_hello_(self):
		self.assertEqual(hello_('michael'), 'hello michael')
		self.assertEqual(hello_(), 'hello world')
	def test_counter(self):
		self.assertEqual(counter(9), 8)

if __name__ == '__main__':
	unittest.main()