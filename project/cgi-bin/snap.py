#!/usr/bin/python

import cgitb,cgi,commands,pwd,random

print "Content-type:text/html"
print ""

cgitb.enable()

data = cgi.FieldStorage()
port=str(random.randint(5900,5999))
port2=str(random.randint(10000,10999))
os = data.getvalue("os")
cpu = data.getvalue("cpu")
ram = data.getvalue("ram")

commands.getoutput("qemu-img create -f qcow2 -b newos.qcow2 snap"+port2+".qcow2")
ec= commands.getstatusoutput("sudo  virt-install  --vnc --vnclisten=192.168.91.130 --vncport="+ port +"  --noautoconsole --name  os"+ port2 +" --ram "+ ram +" --vcpu "+ cpu +" --disk path=/var/lib/libvirt/images/snap"+port+".qcow2,size="+ hd +" --import")

ec1=commands.getstatusoutput("sudo python /var/www/html/websockify-master/run -D "+ port2 +"  192.168.91.130:"+ port)

if ec[0]==0 and ec1[0]==0:
	print (" <a href='http://192.168.91.130/vnc/index.html?host=192.168.91.130&port=" + port2 +"' > Click to access your OS </a>")
)

