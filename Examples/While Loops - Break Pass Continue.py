# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

Total = 10
Counter = 0

while Counter < Total:
    print("=============")
    print("Starting loop")
    print(Counter)

    if Counter == 4:
        break
        #continue
        #pass
    Counter += 1
    print("Ending Loop")
    print("=============")


print("Loop Done")
print(f"FINAL COUNTER NUMBER IS: {Counter}")