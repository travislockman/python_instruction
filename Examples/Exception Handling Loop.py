# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

CarCompanyList = ["Honda", "Ford", "Mazda", "Chrysler", "Kia"]
ListLen = len(CarCompanyList)
counter = 0


while counter <= ListLen:
    try:
        print(CarCompanyList[counter])
        counter += 1
        error = 10/0

    except Exception as e:  # This is lazy, write good code...how can we fix this?
        counter += 1
        print(e)
