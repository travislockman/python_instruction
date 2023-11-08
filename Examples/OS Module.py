# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

import os
import time


os.system("ping 8.8.8.8") # os.system is Very, very powerful, like Obi-Wan powerful, pass any shell command

print("##############")
os.system("ipconfig /all")

print("##############")
print(os.getcwd())  # Find the directory you are in, cross platform

print("##############")
os.chdir(r'c:\\users/travi/Documents') # Change the directory you are in.
print(os.getcwd())

print("##############")
filecheck = (os.path.exists(r'c:\\users/travi/Documents/TACOS')) # Check to see if the path exists.

print("##############")
os.mkdir(r'c:\\users/travi/Documents/TACOS') # Create a directory, regardless of OS

print("##############")
print(os.path.exists(r'c:\\users/travi/Documents/TACOS'))

count = 0   # Creating a while loop to make some files to mess with
while count < 10:
    file = open(r"c:\\users/travi/Documents/TACOS/textfile" + str(count) + ".txt", 'w+')
    file.close()
    count += 1

print("##############")  #Listing the directory
print (os.listdir(r"c:\\users/travi/Documents/TACOS/"))
FileList = (os.listdir(r"c:\\users/travi/Documents/TACOS/"))
print(FileList[1])

print("##############") #Walking the directory and performing logic
for files in os.walk(r"c:\\users/travi/Documents/TACOS/.", topdown=True):
    print(files)

print("##############") # Getting information about files inside, needs interpretation
print(os.stat(r"c:\\users/travi/Documents/TACOS/."))

time.sleep(60) # Putting the program to sleep so I can run my mouth

count = 0  # Let's clean up our mess
while count < 10:
    file = r'c:\\users/travi/Documents/TACOS/textfile' + str(count) + '.txt'
    os.remove(file)  # Using OS to delete the file
    count += 1

os.rmdir(r'c:\\users/travi/Documents/TACOS')  # Removing the directory to clean up.

print("##############")
print(os.path.exists(r'c:\\users/travi/Documents/TACOS'))
print("##############")