#!/usr/bin/python
import subprocess
import sys
import time
OS = sys.platform
fs_encoding  = sys.getfilesystemencoding()
prefix = sys.prefix

#print OS
#print(sys.path)
#print fs_encoding
#print prefix
#print(sys.getprofile())
#print(sys.gettrace())
#print(sys.getdlopenflags())
#print(sys.getcheckinterval())
#sys.exit()
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

def wifi_scan():

	if OS.startswith('darwin'):

		subprocess.call(["airport", "-s"])
		subprocess.call(["airport", "-I"])

	elif OS.startswith('linux'):

		subprocess.call(["iw", "list"])
	else:
		sys.exit()

def folder():
	
	if OS.startswith('darwin'):
		subprocess.call(["mkdir", "mine"])
		print 'folder created'
		time.sleep(0)
		subprocess.call(["rm", "-rf", "mine"])
		print 'folder removed'
	
	elif OS.startswith('linux'):
		subprocess.call(["mkdir", "mine"])
		print 'folder created'
		time.sleep(0)
		subprocess.call(["rm", "-rf", "mine"])
		print 'folder removed'
	
	else:
		sys.exit()



def input():

	if OS.startswith('darwin'):

		answer = raw_input('i see you are on a MAC, would you like to see what i know?:')
		if answer == 'y':
			finder()
			time.sleep(0)
			wifi_scan()
			time.sleep(0)
			subprocess.call(["pwd"])
			time.sleep(0)
			folder()
			
		elif answer == 'n':
			print 'fine then i will keep my secrets!'
		else:
			sys.exit()

	elif OS.startswith('linux'):

		answer0 = raw_input('i see you are using linux, would you like to see what i know?:')
		if answer0 == 'y':
			finder()
			time.sleep(0)
			wifi_scan()
			time.sleep(0)
			subprocess.call(["pwd"])
			time.sleep(0)
			folder()

		elif answer0 == 'n':
			print 'fine then i will keep my secrets!'
		else:
			sys.exit()





input()
#finder()
