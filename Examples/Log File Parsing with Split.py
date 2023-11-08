# Example written by Travis Lockman
# O_o tHe pAcKeTs nEvEr LiE o_O #

sourcefile = open(r"D:\\Python\HackerU\Examples\Candles120.txt")  # r is so so important, it translates into RAW because of backslash


for line in sourcefile:

    parser = line.split(",") # Pay attention to the delimiter
    open = parser[1]

    print(parser)

sourcefile.close() # Always close

