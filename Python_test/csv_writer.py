import csv



# with open('students.csv', 'w') as file:
# 	csv_writer = csv.writer(file)
# 	csv_writer.writerow(['First name', 'Last name', 'Age'])
# 	csv_writer.writerow(['Jack', 'White', 23])
# 	csv_writer.writerow(['Jane', 'Black', 22])


with open('students1.csv', 'w') as file:
	headers_list = ['First name', 'Last name', 'Age']
	csv_writer = csv.DictWriter(file, fieldnames=headers_list)
	# csv_writer.writerow(['First name', 'Last name', 'Age'])
	csv_writer.writeheader()
	csv_writer.writerow({
		'First name' : 'Jack', 
		'Last name' : 'White', 
		'Age' : 23})


	csv_writer.writerow({
		'First name' : 'Jane', 
		'Last name' : 'Black', 
		'Age' : 22})
