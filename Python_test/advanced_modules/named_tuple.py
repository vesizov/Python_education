from collections import namedtuple

jake = ('Jack', 'Smith', 19, 'male')
jim = ('Jim', 'Blade', 23, 'male')
jane = ('Jane', 'Morrison', 20, 'female')

person = namedtuple('person', 'name surname age gender')
jake = person(name='Jake', surname='Smith', age=19, gender='male')# thats fun!!


print(jake.gender)
jake = jake._replace(surname='Blade')
print(jake.surname)