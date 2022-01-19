from collections import Counter

def count_vowels(some_text:str):
	vowels = ('a', 'e', 'i', 'o', 'u')
	cnt = Counter(some_text.lower())
	return sum(char[1] for char in cnt.items() if char[0] in vowels)
	
vowels = ('a', 'e', 'i', 'o', 'u')
number_list = [1,1,1,4,4,5,77,77,3,3,3,3,3]
string ='ddddddkkkkkkkkkkkkiiiiiiiiiipppppooooooo'
sentence = 'Hello, how are you doing? Hello, I\'m fine. How do you do?'

# print(Counter(number_list))
# print(Counter(number_list)[3])

# print(a:=Counter(sentence.lower()))

# gen =(char[1] for char in a.items() if char[0] in vowels)
# print(sum(gen))

def count_vowels(some_text:str):
	vowels = ('a', 'e', 'i', 'o', 'u')
	cnt = Counter(some_text.lower())
	return sum(char[1] for char in cnt.items() if char[0] in vowels)

print(count_vowels(sentence))




# print(a['d'])
# print(Counter(sentence.split()))

# c = Counter(sentence.split())
# c.clear()

# print(list(c))
# print(set(c))
# print(dict(c))

# print(c.items())
# print(Counter(dict(c.items())))

# print(c.most_common()[:-2-1:-1])