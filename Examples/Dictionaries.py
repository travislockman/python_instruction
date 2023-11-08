# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

# creating a dictionary
example_dictionary = {'name': 'Jack', 'age': 26}
print(example_dictionary)

# update value
example_dictionary['name'] = 'John'
example_dictionary['age'] = 27
print(example_dictionary)

# add item
example_dictionary['address'] = ['Downtown','Uptown','Midtown']
print(example_dictionary)
print(example_dictionary['address'][2])

# Remove an Item
example_dictionary.pop('age')
#del example_dictionary['age']
print(example_dictionary)

# Clear all items, but leave dictionary in place
example_dictionary.clear()
print(example_dictionary)

# Remove dictionary completely
del example_dictionary
print(example_dictionary)
