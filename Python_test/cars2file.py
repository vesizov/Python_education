import csv


with open('cars.csv', 'r')  as source_file:
	csv_reader = csv.DictReader(source_file)
	# with open('cars2file.csv', 'w') as result_file:
	# 	csv_writer = csv.writer(result_file)
	# 	csv_writer.writerow(['Make', 'Model'])
	with open('cars2file1.csv', 'w') as result_file:
		
		csv_writer = csv.DictWriter(result_file, fieldnames= ['Make', 'Model'])
		csv_writer.writeheader()
		for car in csv_reader:
			csv_writer.writerow({'Make' :car['Make'], 'Model' : car['Model']})