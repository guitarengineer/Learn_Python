import csv

spamreader = csv.reader(open('transactions.csv'), delimiter=',')
for row in spamreader:
  print ','.join(row)

