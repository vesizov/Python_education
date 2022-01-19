import csv

# num = 3
# with open('/Users/vladimir/Documents/upgrade/Questions.csv') as file:
#     reader = csv.reader(file, delimiter =';')
#     question = next(q for n, q in enumerate(reader) if n == num)
# question




class Believer:
	def __init__(self):
		self.path = None
		self.q_gen = None
		self.score = 0
		self.current_question = None
		self.__end = False


	def set_path(self, path):
		self.path = path
		with open(self.path) as file:
			reader = csv.reader(file, delimiter = ';')
			tmp = [question for question in reader] # Kostil!
			self.q_gen = (question for question in tmp)
		return self

	def next_question(self):
		try:
			self.current_question = next(question for question in self.q_gen)
			return self.current_question[0]
		except StopIteration:
			self.__end = True
			self.current_question = ['Was it fun?', 'Yes', 'It was hard!']
			return self.current_question[0]

	def game(self, user_input:str):
		if user_input == self.current_question[1]:
			self.score += 1
			print(f"Right! {self.current_question[2]}")
		else:
			print(f"No! {self.current_question[2]}")

	def get_state(self):
		return not self.__end

g = Believer()
g.set_path('/Users/vladimir/Documents/upgrade/Questions.csv')

while g.get_state():
	print(g.next_question())
	g.game(input('Yes or No?: '))

print(g.score)




