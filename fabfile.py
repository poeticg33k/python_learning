#!/usr/local/bin/python

from fabric.api import *
import sys
import subprocess

OS = sys.platform
def hello(who="world"):
	print "Hello {who}!".format(who=who)

def host_type():
	run('uname -s')

def dmesg():
	sudo('dmesg')

def wget_install():
	sudo('yum install wget')

def finder(): 
	
	if OS.startswith('darwin'):

	   print OS 
	   print(sys.version)
	   print "Python", (sys.version_info)
	   print(sys.maxsize)
	   subprocess.call(["ls", "-ltr"])
	   subprocess.call(["w"])

        elif OS.startswith('linux'):

 	   print OS 
	   print(sys.version)
	   print "Python", (sys.version_info)
	   print(sys.maxsize)
	   subprocess.call(["ls", "-ltr"])
	   subprocess.call(["w"])
   	
   	else:

	   print  'OS is not supported'

