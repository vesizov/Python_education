import random


dic =[ 
    ('first' , 'True'),
    ('second' , 'False'),
    ('third' , 'True'),
    ('fourth' , 'False')
]

while dic:
    quest = random.choice(dic)
    print(len(dic))
    dic.remove(quest)
    print(':)' if quest[1] == input(f"{quest[0]}: ") else ':[')