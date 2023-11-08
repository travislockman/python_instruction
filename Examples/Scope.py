# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #


number = 5

def myfunction(number):

    #global number
    number += 1
    print(f"number in function is: {number}")
    for i in range(number):
        print("Hello")
    return number # Thank you Pablo!



print(myfunction(number))
print(number)