#!/usr/local/bin/python

import paramiko
 
cmd    = "sudo dmesg"
  
ssh    = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.0.1.8', username='g33k')
stdin, stdout, stderr = ssh.exec_command(cmd)
type(stdin)
stdin.write('this2ismine\n')
stdin.flush()
print stderr.readlines()
print stdout.readlines()
ssh.close()
