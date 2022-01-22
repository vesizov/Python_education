import time

string = list('Спасибо за подписку')


def reverse(array, end=None, counter=0):
    if end is None:
        end = len(array) - 1
    if counter < len(array):
        if array[0] != ' ':
            counter += 1
            array.insert(end, array.pop(0))
            return reverse(array, end, counter)
        else:
            array.pop(0)
            array.insert(len(array) - counter, ' ')
            counter += 1
            return reverse(array, (len(array) - 1) - counter, counter)
    else:
        return ''.join(array)


start_time = time.time()
print(reverse(string), '\n', "--- %s seconds ---" % (time.time() - start_time))


def my_var(text):
    def roll(array, start, stop=None):
        if stop is None:
            stop = len(array) - 1
        array[start:stop + 1] = array[stop:None if start == 0 else (start - 1):-1]
        return ''.join(array)

    l = len(text)
    start = 0

    for i in range(l):
        if text[i] == ' ':
            roll(text, start, i - 1)
            start = i + 1

    roll(text, start)
    return ''.join(text[::-1])


start_time = time.time()
print(my_var(string), '\n', "--- %s seconds ---" % (time.time() - start_time))

string = list('Спасибо за подписку')


def f(s):
    l = len(s)

    def inverse_word(i1, i2):
        for i in range(1 + (i2 - i1) // 2):
            s[i1 + i], s[i2 - i] = s[i2 - i], s[i1 + i]

    inverse_word(0, l - 1)
    i1 = 0
    for i in range(l):
        if s[i] == ' ':
            inverse_word(i1, i - 1)
            i1 = i + 1
    inverse_word(i1, l - 1)

    return ''.join(s)

start_time = time.time()
print(f(string), '\n', "--- %s seconds ---" % (time.time() - start_time))
