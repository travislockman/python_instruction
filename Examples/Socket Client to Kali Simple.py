
# 1	Import both socket and time libraries.
import socket
import time

#3	Connect to the listener by using a socket.socket() object. Create a 30 seconds delay before the socket closes.
s = socket.socket()
s.connect(("192.168.1.123", 4))

print("Connection successful!!!")
time.sleep(30)
s.close()
