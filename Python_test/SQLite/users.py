import sqlite3


connection = sqlite3.connect('users.db')
cursor = connection.cursor()
# create_query = "CREATE TABLE users (user_name TEXT, user_password TEXT);"
# insert_query = "INSERT INTO users VALUES (?, ?)"
# cursor.execute(create_query)

# users = [

# 	('jack123','asdgjgahkljgh'),
# 	('janepretty444', 'asdhfgajk'),
# 	('bobman123', 'ihtgkjhg')
# ]
# cursor.executemany(insert_query,users)

user_name = input('Enter you user_name: ')
user_password = input('pwd: ')

# select_query = f"SELECT * FROM users WHERE user_name = '{user_name}' AND user_password = '{user_password}'"
select_query = "SELECT * FROM users WHERE user_name = ? AND user_password = ?"

cursor.execute(select_query,(user_name, user_password))
data = cursor.fetchone()
print('You are logged in' if data else 'Wrong username or password!')



connection.commit()
connection.close()