
try:

    num1 = 10
    num2 = 0
    div = num1/num2
    print(div)


except ZeroDivisionError as variable:
    print(variable)

else:
    print("No exception happened.")

finally:
    print("This runs everytime.")

# age = 12
# try:
#     if age < 18:
#         raise Exception("The user is younger than 18.")
#
# except ZeroDivisionError as error:
#     print(error)