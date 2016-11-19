#!/usr/bin/python2

#nfs client side
import os

usr = raw_input("Enter your username : ")

# creating folder and mounting storage on client side 
os.system("yum install nfs-utils -y &>/dev/null")
print "Creating and mounting storage in TNdrive on your desktop"
os.system("mkdir  /media/TNdrive")

if os.system(" mount 192.168.91.130:/mnt/" + usr + "  /media/TNdrive") == 0 :
	print "TNdrive is ready for use. "
