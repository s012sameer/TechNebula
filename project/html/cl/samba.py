#!/usr/bin/python2

#samba(CIFS) client side
import os

usr = raw_input("User Name : ")
os.system("yum install cifs-utils -y &>/dev/null")
print "Creating and mounting storage in TNdrive on your desktop"
os.system("mkdir  /media/TNdrive")

# mounting storage on folder created by client
b = os.system(" mount  -o username=" + usr + "  //192.168.91.130/" + usr + "  /media/TNdrive")
if b == 0 :
	print "TNdrive is ready for use. "
