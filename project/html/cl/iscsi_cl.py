#nfs client side
import os

usr = raw_input("Enter your username : ")

#discovery
os.system("iscsiadm --mode discoverydb --type sendtargets --portal 192.168.91.130 --discover")
#login
ec=os.system("iscsiadm --mode node --targetname "+ usr +" --portal 192.168.91.130:3260 --login")
if ec==0:
	print "Storage attached to your system"
