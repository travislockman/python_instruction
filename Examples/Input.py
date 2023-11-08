name = input("Please enter ytype(name)")
age = input("Please enter your age: ")
age_type = type(age)

print(f'Name is: {name}, and variable type is: {name_type}')
print(f'Age is: {age}, and variable type is: {age_type}')

age = 40
age_type = type(age)
print(f'Type is now: {age_type}')