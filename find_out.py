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
		subprocess.call(["ifconfig"])
	else:
		sys.exit()

def folder():
	
	if OS.startswith('darwin'):
		subprocess.call(["mkdir", "mine"])
		print 'folder created'
		time.sleep(0)
		subprocess.call(["touch", "mine/file"])
		print 'file created in mine'
		f = open('mine/file', 'w')
		f.write('this is a file i jsut created\nadding second line\n')
		f.close()
		p = open('mine/file', 'rb').read()
		print p
		time.sleep(5)
		subprocess.call(["rm", "-rf", "mine"])
		print 'folder removed'
	
	elif OS.startswith('linux'):
		subprocess.call(["mkdir", "mine"])
		print 'folder created'
		time.sleep(0)
		subprocess.call(["touch", "mine/file"])
		print 'file created in mine'
		f = open('mine/file', 'w')
		f.write('this is a file i jsut created\nadding second line\n')
		f.close()
		p = open('mine/file', 'rb').read()
		print p
		time.sleep(5)
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


def choices():

	if OS.startswith('darwin'):
		choice = raw_input('this is a mac these are what i can do, enter 1 2 or 3:')
		if choice == '1':
			wifi_scan()
		elif choice == '2':
			finder()
		elif choice == '3':
			folder()
		else:
			print 'ok then, i wont show you!'

	if OS.startswith('linux'):
		choice = raw_input('this is a linux box these are what i can do, enter 1 2 or 3:')
		if choice == '1':
			wifi_scan()
		elif choice == '2':
			finder()
		elif choice == '3':
			folder()
		else:
			print 'ok then, i wont show you!'


choices()
#input()
#finder()
