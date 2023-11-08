# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

import os

IP = ["8.8.8.8", "8.8.4.4", "75.75.75.75"]

for address in IP:
    os.system(f"ping {address}")
