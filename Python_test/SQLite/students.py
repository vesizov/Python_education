import sqlite3


connection = sqlite3.connect('students.db')
cursor = connection.cursor()
insert_query = "INSERT INTO students (first_name, last_name, age) VALUES (?, ?, ?);"

# cursor.execute('CREATE TABLE students (first_name TEXT, last_name TEXT, age INTEGER);')
# cursor.execute('INSERT INTO students (first_name, last_name, age) VALUES ("James", "Brown", 21)')

# fn = 'Jane'
# ln = 'Black'
# age_ = 18


# cursor.execute(f"INSERT INTO students (first_name, last_name, age) VALUES ('{fn}', '{ln}', {age_});") #Bad approach! SQL injection danger!

# cursor.execute("INSERT INTO students (first_name, last_name, age) VALUES (?, ?, ?);",(fn, ln, age_)) #Good approach!

# stud_list = [
# 	('Jane', 'Air', 18),
# 	('Jack', 'Scott', 22),
# 	('Bob', 'Green', 21),
# 	('Jane', 'Ostin', 29)
# ]


# for stud in stud_list:
# 	cursor.execute(insert_query, stud)

# cursor.executemany(insert_query, stud_list) #Thats fun!


# print(tuple(cursor))
# print(cursor.fetchall()) #fetchone
# cursor.execute("UPDATE students SET last_name = 'Austen' WHERE last_name IS 'Ostin'")
cursor.execute("DELETE FROM students WHERE last_name = 'Scott'")
result = cursor.execute("SELECT * FROM students;")
[print(row) for row in result]# Thanks for the idea!



connection.commit()
connection.close()