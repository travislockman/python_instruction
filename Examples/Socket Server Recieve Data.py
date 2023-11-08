# RUN FROM A KALI BOX #

import socket

s = socket.socket()
s.bind(("0.0.0.0", 4444))
s.listen(1)

conn, addr = s.accept()

data = conn.recv(2048).decode()
print(data)
s.close()
