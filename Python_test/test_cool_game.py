import unittest
import cool_game

class CoolGameFunctionsTest(unittest.TestCase):
	def test_greet(self):
		"""
		greet() have to return ***
		"""
		self.assertEqual(cool_game.greet('Jack', False), 'Hello Jack! How are you?')


	def test_greet_enemy(self):
		self.assertEqual(cool_game.greet('Ivan', True), 'Hello Ivan! I will kill you, bastard!')


	def test_eat_burgers(self):
		self.assertEqual(cool_game.eat_burgers(3), 'Mmm! That was excellent!')

	def test_eat_too_much_burgers(self):
		self.assertEqual(cool_game.eat_burgers(4), 'Oh! I overate!')	
if __name__ == '__main__':
	unittest.main()