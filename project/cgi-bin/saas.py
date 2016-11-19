#!/usr/bin/python

import cgitb,cgi,commands,pwd

print "Content-type:text/html"
print ""

cgitb.enable()

data = cgi.FieldStorage()
usr = data.getvalue("name")
passwd = data.getvalue("password")
sw = data.getvalue("software")
cl_ip = cgi.os.environ["REMOTE_ADDR"]

if usr !=None and passwd !=None:
	commands.getstatusoutput("sudo iptables -F")
	a = []
	for p in pwd.getpwall():
		 a.append(p[0])
	if usr in a :
		print "Username Already in use...Try again"
	else:
		commands.getstatusoutput("sudo useradd " + usr)
		ec=commands.getstatusoutput("sudo echo -e " + passwd + " | sudo passwd " + usr + " --stdin")
		if ec[0]==0:
			l = """<html>
	<p><a href="http://192.168.91.130/saasf.html"> Click to browse available softwares </a></p>
	</html> """
			print l
