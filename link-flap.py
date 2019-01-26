
#!/usr/bin/env python

"""link-flap.py: A python script to help some folks with testing. It assumes that the device will log you directly into priviliged mode"""

import argparse
import getpass
import paramiko
import time
import sys

__author__ = "Victor Palacio"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "Github - @vpalacio"

parser = argparse.ArgumentParser(description='Flap an interface.')
parser.add_argument("--username", help="username", required=True)
parser.add_argument("--ip", help="what network device to log into", default='localhost')
parser.add_argument("--port", help="what port to log into", default=22)
parser.add_argument("--interface", help="what port to log into", required=True)
parser.add_argument("--flaps", type=int, help="how many times to flap the interface", default=3)
parser.add_argument("--interval", type=float, help="time in seconds between flaps", default=1)
args = parser.parse_args()

# Establish the connection
remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(args.ip, args.port, username=args.username, password=getpass.getpass(), look_for_keys= False, allow_agent=False)
remote_conn = remote_conn_pre.invoke_shell()
print "SSH connection established"
time.sleep(2)
# output = remote_conn.recv(65535)
# print output

# Set the teminal legnth and go into config mode
print "Going into config mode on " + args.interface + "\n"
remote_conn.send("terminal length 0\n")
remote_conn.send("conf t\n")
remote_conn.send("interface " + args.interface + "\n")
time.sleep(2)
# output = remote_conn.recv(65535)
# print output

print "Flapping ports for " + str(args.flaps) + " times\n"
for i in range(args.flaps):
    remote_conn.send("shut\n")
    time.sleep(args.interval)
    remote_conn.send("no shut\n")
    time.sleep(args.interval)

time.sleep(2)
# output = remote_conn.recv(65535)
# print output

# Close the connection
print "Close the connection and print the buffer"
remote_conn.send("end\n")
time.sleep(1)
remote_conn.close()
output = remote_conn.recv(65535)
print output

sys.exit("operation completed")