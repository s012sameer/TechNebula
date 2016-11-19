#!/usr/bin/python

import cgitb,cgi,commands,pwd,random

print "Content-type:text/html"
print ""

cgitb.enable()

data = cgi.FieldStorage()
port=str(random.randint(5900,5999))
port2=str(random.randint(7000,9999))
os = data.getvalue("os")
cpu = data.getvalue("cpu")
ram = data.getvalue("ram")

ec= commands.getstatusoutput("sudo  virt-install  --vnc --vnclisten=192.168.91.130 --vncport="+ port +"  --noautoconsole --name  os"+ port2 +" --ram "+ ram +" --vcpu "+ cpu +" --nodisk --cdrom /ubuntu.iso")

ec1=commands.getstatusoutput("sudo python /var/www/html/websockify-master/run -D "+ port2 +"  192.168.91.130:"+ port)

if ec[0]==0 and ec1[0]==0:
	print (" <a href='http://192.168.91.130/vnc/index.html?host=192.168.91.130&port=" + port2 +"' > Click to access your OS </a>")


