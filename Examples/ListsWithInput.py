# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

# Fritanga

list1 = ["Carne Asada", "Carne Desmenuzada", "Pollo a la parrilla"]
list2 = ["Maduros", "Tajadas", "Queso Frito"]

print(list1)
print(list2)

print(f"{list1[1]} con {list2[2]}")

list2.append("Repollo")
print(list2)

list2[0] = "Crema"
print(list2)

del list2[3]
print(list2)

userdecision = input("Do you want to delete the list(Y/N): ")
print(userdecision)

if userdecision == "Y" or userdecision == "y":
    del list2
elif userdecision == "N" or userdecision == "n":
    print("Your data is safe!")
else:
    print("You entered something wrong dummy...")

print(list2)
