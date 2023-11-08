# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

# Fritanga

list1 = ["Carne Asada", "Carne Desmenuzada", "Pollo a la parrilla"]
list2 = ["Maduros", "Tajadas", "Queso Frito"]

print(list1)
print(list2)

print(f"{list1[1]} with {list2[2]}")

list2.insert(2, "Repollo")
print(list2)
list2.append("Chile")
list2.remove("Tajadas")
print(list2)

list2[0] = "Crema"
print(list2)

# del list2[3]
# print(list2)

del list2
print(list2)
