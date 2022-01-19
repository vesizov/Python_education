from collections import Counter

def is_full_house(combination: list):
	# ctn = Counter(combination)
	state = Counter(combination).most_common(2)
	return state[0][1]==3 and state[1][1] == 2


print(is_full_house(['A', 'A', '3', 'J', 'A']))



# def count_vowels(some_text:str):
# 	vowels = ('a', 'e', 'i', 'o', 'u')
# 	cnt = Counter(some_text.lower())
# 	return sum(char[1] for char in cnt.items() if char[0] in vowels)
	
# vowels = ('a', 'e', 'i', 'o', 'u')
# number_list = [1,1,1,4,4,5,77,77,3,3,3,3,3]
# string ='ddddddkkkkkkkkkkkkiiiiiiiiiipppppooooooo'
# sentence = 'Hello, how are you doing? Hello, I\'m fine. How do you do?'