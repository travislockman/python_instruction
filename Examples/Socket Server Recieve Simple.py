# RUN FROM A KALI BOX #

import socket

s = socket.socket()
s.bind(("0.0.0.0", 4444))
s.listen(1)

conn, addr = s.accept()
s.close()