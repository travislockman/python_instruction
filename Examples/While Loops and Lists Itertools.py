# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

import itertools

Strategy_List = []

TAKE_PROFIT_Start = int(input('Please enter the Take Profit Start Range (Format 25): '))
TAKE_PROFIT_End = int(input('Please enter the Take Profit End Range (Format 25): '))
TAKE_PROFIT_Multiplier = int(input('Please enter the Take Profit Multiplier (Format 1): '))

STOP_LOSS_Start = int(input('Please enter the Stop Loss Start Range (Format 25): '))
STOP_LOSS_End = int(input('Please enter the Stop Loss End Range (Format 25): '))
STOP_LOSS_Multiplier = int(input('Please enter the Stop Loss Multiplier (Format 1): '))

TAKE_PROFIT_List = []

while TAKE_PROFIT_Start <= TAKE_PROFIT_End:
    TAKE_PROFIT_List.append(TAKE_PROFIT_Start)
    TAKE_PROFIT_Start = TAKE_PROFIT_Start + TAKE_PROFIT_Multiplier
Strategy_List.append(TAKE_PROFIT_List)

STOP_LOSS_List = []
while STOP_LOSS_Start <= STOP_LOSS_End:
    STOP_LOSS_List.append(STOP_LOSS_Start)
    STOP_LOSS_Start = STOP_LOSS_Start + STOP_LOSS_Multiplier
Strategy_List.append(STOP_LOSS_List)

permuatations = list(itertools.product(*Strategy_List))

print(permuatations)
length = len(permuatations)
print(length)

