import random


class HangedMan:
    def __init__(self, file_path, tries=2):
        self.file_path = file_path
        self._tries = tries
        self.__word = None
        self.user_word = None
        self.user_chars = set()

    def set_number_of_tries(self, number: int):
        self._tries = number

    def get_tries(self):
        return self._tries

    def word_gen(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            self.__word = list(self.random_word(file).strip('\n'))
        self.user_word = ['-' for _ in self.__word]

    def guess_char(self, char):
        if char not in self.__word:
            self.user_chars.add(char)
            self._tries -= 1
            print(f"No such character in your word, you have {self.get_tries()} tries left\n {''.join(self.user_word)}")
        else:
            char_idx = (idx for idx, _char in enumerate(self.__word) if _char == char)

            for idx in char_idx:
                self.user_word[idx] = char
            print(f"Bingo! And you still have {self.get_tries()} tries left \n {''.join(self.user_word)}")

    def guess(self, guess):
        if self.__word == list(guess):
            self.user_word = self.__word
        else:
            self._tries -= 1
            print(f"Of course not, you have {self.get_tries()} tries left \n {''.join(self.user_word)}")

    def play(self, string):
        self.guess(string) if len(string) > 1 else self.guess_char(string)

    def get_user_chars(self):
        return sorted(self.user_chars)

    @property
    def the_end(self):
        if sorted(self.__word) == sorted(self.user_word):
            print('Epic Win!')
            return True
        elif self._tries == 0:
            print(f'Looser! it was\n {"".join(self.__word)}')
            return True
        else:
            return False

    @staticmethod
    def random_word(file):
        try:
            line = next(file)
            for num, aline in enumerate(file, 2):
                if random.randrange(num):
                    continue
                line = aline
            return line
        except StopIteration:
            print('Something is wrong!')


g = HangedMan('/Users/vladimir/Documents/upgrade/WordsStockRus.txt', 7)
g.word_gen()


while not g.the_end:
    g.play(input('Enter: '))
    print(g.get_user_chars())
