import csv

# with open('cars.csv')  as file:
# 	csv_reader = csv.reader(file)
# 	for car in csv_reader:
# 		# print(car)
# 		print(f'{car[1]}  {car[4]}')



# with open('cars.csv')  as file:
# 	csv_reader = csv.reader(file)
# 	data_list = list(csv_reader)
# 	print(data_list)



with open('cars.csv')  as file:
	csv_reader = csv.DictReader(file)
	for car in csv_reader:
		print(f'{car["Make"]} {car["Model"]}  {car["Price"]}')