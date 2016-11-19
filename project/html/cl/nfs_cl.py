#!/usr/bin/python

import commands

commands.getstatusoutput("yum install nfs-utils -y &>/dev/null")
usr = raw_input("User name : ")
print "Creating and mounting storage in TNdrive on your desktop"
commands.getstatusoutput("mkdir  /media/TNdrive")

if os.system(" mount 192.168.91.130:/mnt/" + usr + "  /media/TNdrive") == 0 :
	print "Your storage is ready...mounted on your desktop. "
