#!/usr/bin/python

import socket

def change_identify(tor_password="",tor_control_socket="/var/run/tor/control",
tor_cookie="/var/run/tor/control.authcookie",tor_host="localhost",tor_port=9051):

	try:

		if len(tor_password):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((tor_host, tor_port))
			
			token=tor_password
			
		else:
			s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
			s.connect("/var/run/tor/control")

			f=open("/var/run/tor/control.authcookie")

			token=f.read()

		s.send('AUTHENTICATE "%s"\n' % (token))
		
		out=s.recv(1024)
		if out.split(" ")[0]!="250":print out;return False

		s.send("SIGNAL NEWNYM\n")
		out=s.recv(1024)
		if out.split(" ")[0]!="250":print out;return False

		s.send("QUIT\n")
		out=s.recv(1024)
		if out.split(" ")[0]!="250":print out;return False
		
		f.close()
		s.close()
		
		return True
	except Exception as e:
		print "[EE] "+e.message
		
if __name__ == '__main__':
	if change_identify():
		print "Done"
	else:
		print "Fail"
