#!/usr/bin/python2

import commands,cgi,pwd,cgitb
#samba server side

print "Content-type:text/html"
print ""

cgitb.enable()


data = cgi.FieldStorage()
usr = data.getvalue("name")
passwd = data.getvalue("password")
lvsize = data.getvalue("size")

if usr !=None and passwd !=None and lvsize != None:
	a = []
	for p in pwd.getpwall():
		 a.append(p[0])
	if usr in a :
		print "Username already used. Try again..."	
	else:
		commands.getstatusoutput("sudo iptables -F")
		commands.getstatusoutput("sudo lvcreate --name " + usr + " -V" + lvsize + "G  cloudvg/pool ")
		commands.getstatusoutput("sudo mkfs.xfs   /dev/cloudvg/" + usr)		
		commands.getstatusoutput("sudo mkdir /mnt/" + usr + " ; sudo chmod 777 /mnt/" + usr)		
		ec = commands.getstatusoutput("sudo mount /dev/cloudvg/" + usr + " /mnt/" + usr )		
		# creating user and password
		commands.getstatusoutput("sudo useradd " + usr)
		commands.getstatusoutput("sudo echo  -e '"+passwd+"\n"+passwd+"' | sudo smbpasswd  -a " + usr )

		# edit in configuration file of samba server
		f = open("/etc/samba/smb.conf","a")   
		f.write("\n[" + usr + "] \npath=/mnt/" + usr + "\nwritable=yes\n")
		f.close()
		commands.getstatusoutput("sudo systemctl restart smb")

		if  ec[0] == 0:
			s = """ <html>
				<a href="http://192.168.91.130/samba.tar" > Click to download setup </a>
				</html>
				"""
			print s
		else:
			print "Error"

else:
	print "All fields are mandatory"	
