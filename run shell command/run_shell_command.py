#!/usr/bin/python
#this will demonstrate how to run a shell command from python

import os
import subprocess

print """choose method to run a shell command
    1. os.system(command with args)
    2. call() from subprocess module
    """

choice = raw_input("enter your choice:")

if choice == "1": 
    print "you chose 1"
    print "enter a shell command"
    command = raw_input("command: ")
    os.system(command)
elif choice == "2":
    print "you chose 2"
    print "enter a shell command"
    command = raw_input("command: ")
    subprocess.call([command])
    else:
    print  "%r is not a good choice" % choice

 
