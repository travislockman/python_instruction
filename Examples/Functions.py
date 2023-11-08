# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #


def calc(num1, num2, operation):
    if operation == "addition":
        total = int(num1) + int(num2)
    elif operation == "subtraction":
        total = int(num1) - int(num2)
    elif operation == "division":
        total = int(num1) / int(num2)
    elif operation == "multiplication":
        total = int(num1) * int(num2)
    elif operation == "exponent":
        total = int(num1) ** int(num2)
    elif operation == "modulo":
        total = int(num1) % int(num2)
    else:
        print("ERROR, PLEASE DON'T BE DUMB...")
        total = "ERROR"
    output_list = [total, num1, num2, operation]
    return output_list


asknum = input("Please give me a number: ")
asknum2 = input("Please give me another number: ")
askop = input("Please give me the operation (Addition,Subtraction,Multiplication,Division,Exponent,Modulo:) ").lower()

add_total = calc(asknum,asknum2,askop)
print(type(add_total))
print(add_total)

print("###########################################################")
print(f"Your Total Is: {add_total[0]}")
print(f"Your First Number Was: {add_total[1]}")
print(f"Your Second Number Was: {add_total[2]}")
print(f"Your Operation Was: {add_total[3]}")
print("###########################################################")








