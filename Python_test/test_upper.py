import unittest
import upper


class TestUpper(unittest.TestCase):
	
	def test_one_word(self):
		text = 'hello!'
		result = upper.upper_text(text)
		self.assertEqual(result,'HELLO!')
		self.assertNotEqual(result,'Hello!')

	def test_multiple_words(self):
		text='hello world!'
		result = upper.upper_text(text)
		self.assertEqual(result,'HELLO WORLD!')

if __name__ == '__main__':
	unittest.main()
