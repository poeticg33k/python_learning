#!/usr/local/bin/python

import paramiko 
import sys
import os

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.0.1.8', username='g33k')
stdin, stdout, stderr = ssh.exec_command("uptime")
type(stdin)
print stdout.readlines()
stdin, stdout, stderr = ssh.exec_command("cat .zshrc")
type(stdin)
print stdout.read()
stdin, stdout, stderr = ssh.exec_command("sudo demsg")
type(stdin)
stdin.write('#14t3d1iam\n')
stdin.flush()
print stdout.read()
#data = stdout.read().splitlines()
#for line in data:
#	if line.split(':')[0] == 'AirPort':
 #		print line

