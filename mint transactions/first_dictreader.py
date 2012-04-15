#import transactions.csv using dictreader and print out some stuff

import csv

# set filename and label names (should match header row of csv file)
filename = 'transactions.csv'
labels = ['date','description','original_description','amount', \
          'transaction_type','category','account_name','labels','notes']

print "These are the categories:"
for i in labels:
  print i

#open the file
mintdata = open(filename, 'rb')

reader = csv.DictReader(mintdata, labels)

#print the entire file, if you so desire
#for row in reader:
#  print row

query = [(item["date"], item["amount"], item["description"]) for item in reader if item["description"] == "AES"]

mintdata.close()

print "\n".join(["%s\t%s\t%s" % (item) for item in query])


