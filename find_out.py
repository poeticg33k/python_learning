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
if OS.startswith('darwin'):
	print 'this will work'
else:
	print  'OS is not supported'

