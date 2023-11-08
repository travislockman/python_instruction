# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

import socket

mysocket = socket.socket()
mysocket.connect(("192.168.1.123", 3500))
mysocket.send("I DID IT FOR THE MEMES!!!\n".encode())
mysocket.close()
