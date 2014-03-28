#!/usr/bin/python
import subprocess
import sys
OS = sys.platform
fs_encoding  = sys.getfilesystemencoding()
prefix = sys.prefix

#print OS
#print(sys.path)
#print fs_encoding
#print prefix

#first attempt
def finder(): 
	
	if OS.startswith('darwin'):

	   print OS 
	   print(sys.version)
	   print(sys.version_info)
	   print(sys.maxsize)
	   subprocess.call(["ls", "-ltr"])
	   subprocess.call(["w"])

        elif OS.startswith('linux'):

 	   print OS 
	   print(sys.version)
	   print(sys.version_info)
	   print(sys.maxsize)
	   subprocess.call(["ls", "-ltr"])
	   subprocess.call(["w"])
   	
   	else:

	   print  'OS is not supported'


def input():

	if OS.startswith('darwin'):

		answer = raw_input('i see you are on a MAC, would you like to see what i know?:')
		if answer == 'y':
			finder()
	#	else:
	#		sys.exit()

	elif OS.startswith('linux'):

		answer2 = raw_input('i see you are using linux, would you like to see what i know?:')
		#print (answer2)
		if answer2 == 'y':
			finder()
		#else:
		#	sys.exit()





input()
#finder()
