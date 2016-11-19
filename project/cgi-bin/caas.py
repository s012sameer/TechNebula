#!/usr/bin/python

import cgitb,cgi,commands,random

print "Content-type:text/html"
print ""

cgitb.enable()

data = cgi.FieldStorage()
num = data.getvalue("no")

commands.getoutput("sudo systemctl restart docker")
print "access your containers using links:"
print "<br>"
for i in range(int(num)):
	port=str(random.randint(6000,7000))
	commands.getoutput("sudo docker run -it -p "+ port +":4200 -d sameeros")
	print (" <a href='http://192.168.91.130:" + port +"' target='_blank'> Container " + str(i) +"</a>")
	print "<br>"
print "<br>"
print "<br>"
print "Access containers using < login - root ; password - technebula >"

