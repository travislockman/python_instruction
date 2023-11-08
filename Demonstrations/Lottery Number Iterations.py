

Main = (int(input("Please enter amount of main numbers, for example Powerball is 5: ")) + 1)
Mult = (input("Use a multiplier number? (Y/N) ")).upper()
Main_Limit = (int(input("Please enter the amount of numbers for the main group, such as 70: ")) + 1)
Mult_Limit = (int(input("Please enter the amount of numbers for the multiplier, such as 25: ")) + 1)
Main_List = []
Mult_List = []
Main_Range = range(1,Main)
Main_Numbers_Range = range(1,Main_Limit)
Mult_Numbers_Range = range(1,Mult_Limit)


for num in Main_Range:
    Main_List.append([])

while True:
    if Mult == "Y":
        Main_List.append([])
        break
    elif Mult == "N":
        break
    else:
        print("YOU NEED TO ENTER 'Y' OR 'N' PLEASE!!!")
        Mult = (input("Use a multiplier? (Y/N) ")).upper()

Main_List_Length = len(Main_List)
if Mult == "Y":
    Main_Print_Limit = Main - 1

else:
    Main_Print_Limit = Main - 1

Main_List_Pos = 0
for num in range(Main_Print_Limit):
    # Just use random
    for number in Main_Numbers_Range:
        Main_List[Main_List_Pos].append(number)
    if Main_List_Pos <= Main_Print_Limit:
        Main_List_Pos += 1



print(Main_List)
print(Main_List_Length)










