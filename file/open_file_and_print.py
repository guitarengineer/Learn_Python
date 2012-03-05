#open a text file and print it, line by line

from sys import argv
script, filename = argv

targetfile = open(filename)

try:
	for line in targetfile:
		print line
finally:
	targetfile.close(
