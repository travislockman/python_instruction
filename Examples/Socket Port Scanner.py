# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

import socket

port_range = range(1, 65535)
file = open('openports.txt', 'w')
file.close()

# for port in port_range:
for port in port_range:
    try:
        s = socket.socket()
        scan = s.connect(("192.168.1.123", port))

    except ConnectionRefusedError as portclosed:
        pass
        # print("Port Closed...moving on.")
    else:
        #print("FOUND OPEN PORT!!!!")
        with open('openports.txt', 'a') as file:
            file.write(str(port))
        s.close()



