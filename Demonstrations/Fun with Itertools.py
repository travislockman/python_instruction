# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

import itertools


Strategy_List = [[10,11,12,13,14,15],[25,26,27,28,29,30],[25,26,27,28,29,30],[25,26,27,28,29,30],[25,26,27,28,29,30]]


print(Strategy_List)

permuatations = list(itertools.product(*Strategy_List))

print(permuatations)
length = len(permuatations)
print(length)