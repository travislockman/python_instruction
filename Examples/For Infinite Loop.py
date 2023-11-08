



num_list = [1, 2, 3, 4]
counter = 0
for num in num_list:
    num_list.append(num)
    counter += 1
    list_length = len(num_list)
    print(num_list)
    print(f"This is pass: {counter}")
    print(f"The length of the list is: {list_length}")
