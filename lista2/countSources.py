import csv


with open('csv.csv', newline='') as file:
	reader = csv.reader(file, delimiter=',', quotechar='|')
	for row in reader:
		print(row[5])

