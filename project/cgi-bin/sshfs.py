#!/usr/bin/python

import cgitb,cgi,commands,pwd

print "Content-type:text/html"
print ""

cgitb.enable()

#cl_ip = cgi.os.environ["REMOTE_ADDR"]
data = cgi.FieldStorage()
usr = data.getvalue("name")
passwd = data.getvalue("password")
lvsize = data.getvalue("size")

if usr !=None and passwd !=None and lvsize != None:
	a = []
	for p in pwd.getpwall():
		 a.append(p[0])
	if usr in a :
		print "Username already in use. Try again..."
	else:
		commands.getstatusoutput("sudo iptables -F")
		commands.getstatusoutput("sudo useradd " + usr)
		commands.getstatusoutput("sudo echo -e " + passwd + " | sudo passwd " + usr + " --stdin")
		commands.getstatusoutput("sudo lvcreate --name " + usr + " -V +" + lvsize + "G  cloudvg/pool ")
		commands.getstatusoutput("sudo mkfs.xfs   /dev/cloudvg/" + usr)		
		commands.getstatusoutput("sudo mkdir /mnt/" + usr + " ; sudo chmod o+rwx /mnt/" + usr)		
		ec = commands.getstatusoutput("sudo mount /dev/cloudvg/" + usr + " /mnt/" + usr )
		if  ec[0] == 0:
			s = """ <html>
				<a href="http://192.168.91.130/sshfs.tar" > Click to download download setup </a>
				</html>
				"""
			print s

else:
	print "All fields are mandatory"


