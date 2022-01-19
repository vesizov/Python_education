import csv

def print_students():
	with open('students.csv','r') as file:
		csv_reader = csv.reader(file)
		for raw in csv_reader:
			print(raw)

print_students()