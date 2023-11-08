# Lottery Number Generator
# Written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

import random

Run_Count = 1

while True:

    if Run_Count == 1:
        Cont = input("Welcome to the Lottery Number Generator! Continue? (Y/N)? ").upper()
        Run_Count += 1
    elif Run_Count > 1:
        Cont = input("Would you like to run it again? (Y/N)? ").upper()

    if Cont == "Y":  # This is for WW.
        pass
    elif Cont == "N":
        print("Thanks for playing and GOOD LUCK!!!")
        break
    else:
        print("YOU NEED TO ENTER 'Y' OR 'N' PLEASE!!!")
        continue

    Main = (int(input("Please enter amount of main numbers, for example Powerball is 5: ")) + 1)
    Mult = (input("Use a multiplier number? (Y/N) ")).upper()
    Main_Limit = (int(input("Please enter the amount of numbers for the main group, such as 70: ")) + 1)
    Main_List = []
    Mult_List = []
    Main_Range = range(1, Main)

    for num in Main_Range:
        Main_List.append([])

    while True:
        if Mult == "Y":
            Mult_Limit = (int(input("Please enter the amount of numbers for the multiplier, such as 25: ")) + 1)
            Main_List.append([])
            Main -= 1
            break
        elif Mult == "N":
            Main -= 1
            break
        else:
            print("YOU NEED TO ENTER 'Y' OR 'N' PLEASE!!!")
            Mult = (input("Use a multiplier? (Y/N) ")).upper()

    Main_List_Length = len(Main_List)
    Main_List_Pos = 0

    for num in range(Main):

        if Main_List_Pos <= Main:
            Number = random.randint(1, Main_Limit)
            Main_List[Main_List_Pos].append(Number)
            Main_List_Pos += 1

    if Mult == "Y":
        Number = random.randint(1, (Mult_Limit - 1))
        print("ADDING MULTIPLIER!!!!")
        Main_List[Main_List_Length - 1].append(Number)

    print(Main_List)
    print("\n")










