#!/usr/bin/python

import cgitb,cgi,commands,pwd,random

print "Content-type:text/html"
print ""

cgitb.enable()
port=str(random.randint(6000,7000))
data = cgi.FieldStorage()
pf = data.getvalue("pf")

commands.getstatusoutput("sudo systemctl restart docker")
commands.getstatusoutput("sudo docker run -it -p "+port+":4200 -d sameer")
if pf == "python":
	print (" <a href='http://192.168.91.130:"+port+"' target='_blank'> Click to get python interpretor </a>")
	print "<br>"
	print "Access bash < login: user  ;    password:redhat >"
elif pf == "bash":
	print (" <a href='http://192.168.91.130:"+port+"' target='_blank'> Click to get bash shell </a>")
	print "<br>"
	print "Access bash < login: client  ;    password:redhat >"
