#!/usr/bin/python

import cgitb,cgi,commands,pwd

print "Content-type:text/html"
print ""

cgitb.enable()


data = cgi.FieldStorage()
cl_ip = cgi.os.environ["REMOTE_ADDR"]
usr = data.getvalue("name")
passwd = data.getvalue("password")
lvsize = data.getvalue("size")

if usr !=None and passwd !=None and lvsize != None:
	a = []
	for p in pwd.getpwall():
		 a.append(p[0])
	if usr in a :
		print "Username not available. Try again"
	else:
		commands.getstatusoutput("sudo iptables -F")
		commands.getstatusoutput("sudo lvcreate --name " + usr + " -V +" + lvsize + "G  cloudvg/pool ")

	# editing config file of nfs server
		f = open("/etc/tgt/conf.d/lv.conf","a")
		f.write("\n<target "+ usr +">\nbacking-store  /dev/cloudvg/" + usr + "\ninitiator-address  "+ cl_ip +"\n</target>")
		f.close()
		ec=commands.getstatusoutput("sudo systemctl restart tgtd")
		
		if ec[0]==0:
			s = """ <html>
				<a href="http:192.168.91.130/iscsi.tar" > Click to download download setup </a>
				</html>
				"""
			print s

		else: 
			print "Error"
else:
	print "All fields are mandatory"
