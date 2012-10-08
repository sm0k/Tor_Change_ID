#!/usr/bin/python

# Must be run through a tor proxychains 

import socket
from termcolor import colored
import requests
import time

def change_identity(tor_password="",tor_control_socket="/var/run/tor/control",
tor_cookie="/var/run/tor/control.authcookie",tor_host="localhost",tor_port=9051,debug=False,sleep_time=0.5):

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

		if debug:
			r=requests.get("http://ifconfig.me",headers={"User-Agent":"curl"})
			print colored("[**] New identity : "+r.content, 'green')

		time.sleep(sleep_time)
		return True
	except Exception as e:
		print "[EE] "+e.message
		
if __name__ == '__main__':
	change_identity(debug=True)
