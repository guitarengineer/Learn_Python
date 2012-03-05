#use this script to compile a .py file to a .pyc and make it executable

import py_compile 			#get the compile module
import sys 					#get the system module for argv
import os 					#get os so we can call chmod

if len(sys.argv) != 3: 
#if the user didnt pass the correct amount of arguments
    print "usage:", sys.argv[0],"infile","outfile" 
    #show them how to use it
    quit() 
    #and exit

infile = sys.argv[1]
outfile = sys.argv[2]

py_compile.compile(infile, outfile) 
#compile the .py to a .pyc (or whatever extension specified)

chmod_macro = "chmod +x " + outfile
#this command will allow the user to execute the outfile with a ./outfile

os.system(chmod_macro) 
#execute the chmod macro

print "success!" 
#and if all went well, inform the user and quit  

