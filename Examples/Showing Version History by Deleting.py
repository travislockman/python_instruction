# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

import os
import time

file_count = 0
file_limit = 10
static_filename = "NewFile"

while file_count < file_limit:
    file_count_string = str(file_count) # Why am I doing this?
    file_name = static_filename + file_count_string + ".txt"
    file = open(file_name, 'w+')

    # More logic working with the file would go here.

    time.sleep(2)
    file_count += 1
    file.close()
    os.remove(file_name)
