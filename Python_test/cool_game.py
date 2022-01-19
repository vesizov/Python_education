def greet(name, isEnemy):
	if isEnemy:
		return f'Hello {name}! I will kill you, bastard!'
	else:
		return f'Hello {name}! How are you?'


def eat_burgers(number):
	return 'Mmm! That was excellent!' if number < 4 else 'Oh! I overate!'