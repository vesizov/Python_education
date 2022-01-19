from collections import defaultdict

# my_dict = {1:'a'}
# my_defaultdict = defaultdict(lambda : None)
# my_defaultdict[1] = 'a'

# print(my_defaultdict[3])
# print(my_dict[1])

# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = defaultdict(list)

# for k, v in s:
#     d[k].append(v)

# print(sorted(d.items()))

# s = 'mississippi'
# d = defaultdict(int)

# for k in s:
#     d[k] += 1
# print(sorted(d.items()))



d = defaultdict(lambda:'<missing>')

d.update(name='John', action='ran')
# print(d.get('action'))

print(f"{d['name']} {d['action']} to {d['obj']}")
print(d)
