import csv


with open('country.csv', newline='') as file:
	reader = csv.reader(file, delimiter=',', quotechar='|')
	for row in reader:
		print(row[7])

