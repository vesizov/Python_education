import csv

def add_student(first_name, last_name, age):
	with open('stud.csv', 'a') as file:
		csv_writer = csv.writer(file)
		csv_writer.writerow([first_name, last_name, age])

add_student(*input('first_name, last_name, age: ').split(','))
