#import a search path into python

import sys
import os

if len(sys.argv) != 2:
	print "usage:", sys.argv[0], "<path to add to python's search path>"
	#instructions to the user 
	quit()
	#exit 

path = sys.argv[1]

sys.path.append(path)
print "added this path to PYTHONPATH", path


