#!/usr/bin/python

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

        elif OS.startswith('linux2'):

 	   print OS 
	   print(sys.version)

        else:

	   print  'OS is not supported'

finder()
