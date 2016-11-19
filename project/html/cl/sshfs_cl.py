#!/usr/bin/python

import commands

commands.getstatusoutput("yum install fuse-sshfs -y &>/dev/null")
print "Creating and mounting storage in TNdrive on your desktop"
commands.getstatusoutput("mkdir  /media/TNdrive")
usr=raw_input("Enter your username : ")
ec=commands.getstatusoutput(" sshfs " + usr + "@192.168.91.130:/mnt/" + usr + "  /media/TNdrive" )
if ec[0] == 0 :
	print "TNdrive ready for use. "
