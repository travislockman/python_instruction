# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

#print(dir(__builtins__)) DO IN IDLE TO SHOW ALL BUILTINS

import random


def printname(firstname, lastname, Status = "Alive"):
    # print(f"Hidden name variable is set to: {__name__}")
    return firstname,lastname,Status,__name__

if __name__ == '__main__':
    print("#####################################")
    result = printname("Travis", "Lockman")
    print(result)
    print("WE ARE IN THE MAIN")
    print(printname("John", "Smith", "Dead"))
    print("#####################################")
