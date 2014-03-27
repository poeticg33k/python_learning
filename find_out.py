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

        elif OS.startswith('linux'):

 	   print OS 
	   print(sys.version)
	   print(sys.version_info)
	   print(sys.maxsize)
	   subprocess.call(["ls", "-ltr"])
   	
   	else:

	   print  'OS is not supported'




finder()
