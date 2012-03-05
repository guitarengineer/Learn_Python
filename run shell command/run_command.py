#!/usr/bin/python
#another way to run a shell command from python

import os
import sys

if len(sys.argv) != 2: 
#if the user didnt pass the correct amount of arguments
    print "usage:", sys.argv[0],"command" 
    #show them how to use it
    quit() 
    #and exit

command = sys.argv[1]

print os.system(command)

