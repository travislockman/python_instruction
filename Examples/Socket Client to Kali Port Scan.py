
# 1	Import both socket and time libraries.
import socket
import time

#3	Connect to the listener by using a socket.socket() object. Create a 30 seconds delay before the socket closes.
s = socket.socket()

for p in range(1,65535):

    try:
        time.sleep(1)
        print(f"CURRENT PORT IS: {p}")
        s.connect(("192.168.1.123", p))


    except ConnectionRefusedError as e:
        print("The connection was refused.")
        print(e)
        print(f"The port is: {p}")

    # except Exception as e:
    #     print("LOOKS LIKE SOMETHING WENT WRONG!!!")
    #     time.sleep(1)
    #     print(e)

    else:
        print("FOUND OPEN PORT!!!")
        print(f"The port is: {p}")
        s.close()


s.close()
