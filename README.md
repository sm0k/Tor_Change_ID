###################################################################
CONFIGURATION
###################################################################
Should set these settings in /etc/tor/torrc :

ControlPort 9051 + password
or 
CookieAuthentication 1

###################################################################
USAGE
###################################################################

proxychains ./change_identity.py


you can also invoke the function from a python script:


change_identity(tor_password="",
		tor_control_socket="/var/run/tor/control",
		tor_cookie="/var/run/tor/control.authcookie",
		tor_host="localhost",
		tor_port=9051,
		debug=False,
		sleep_time=0.5)
