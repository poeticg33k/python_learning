#!/usr/bin/python

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('SERVER NAME', username='')
stdin, stdout, stderr = ssh.exec_command("uptime")
type(stdin)
print stdout.readlines()
stdin, stdout, stderr = ssh.exec_command("cat jvanni201")
type(stdin)
print stdout.read()

#stdin.flush()
#data = stdout.read.splitlines()
#for line in data:
#	if line.split(':')[0] == 'AirPort':
#		print line

