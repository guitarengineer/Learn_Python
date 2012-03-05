#show how to open a CSV

import csv
with open('transactions.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
		print row
