# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

salary = input("How much do you make a year? \n")
bonus = input("How much do you make in bonus? \n")
salary = int(salary)
bonus = int(bonus)

totalsalary = salary + bonus

#OLD WAY
txt4 = "I make ${} a year, my base is {}".format(totalsalary, salary)
#NEW WAY
txt5 = f"I make ${totalsalary} a year, my base is {salary}"  # USE THIS NOW, THE NEW WAY!!!!

print(txt4)
print(txt5)
