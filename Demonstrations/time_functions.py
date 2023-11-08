# Function to Manipulate DateTime and Return Usable Strings and Integers
# T. Lockman
# April 2018
# O_o tHe pAcKeTs nEvEr LiE o_O #

# Importing Modules #

import datetime  # Importing the datetime module

# ####Getting Current Date and Manipulating it for Queries#### #

Current_Date = datetime.date.today()  # Assigns current date to a variable
Current_Date_String = str(Current_Date)  # Converts the date to a string and stores it as a variable
MonthYear = (Current_Date_String[:7])  # Parses the date and cuts the day off and leaves year and month


Year = (Current_Date_String[:4])  # Parses the date and leaves only the year behind
YearInt = int(Year)  # Converts year to a string

Month = MonthYear[5:]
MonthInt = int(Month)  # Parses just the month and year, takes the month only, converts to integer for math

Day = (Current_Date_String[8:])
DayInt = int(Day)  # Takes the date and converts it to an integer for math

Last_MonthYearInt = (MonthInt - 1)  # Takes the month integer and subtracts one to get last month
Last_MonthYear_String = str(Year) + "-" + str(Last_MonthYearInt)  # Combines year and last month to form a string




def fulldate():
    return Current_Date

def today():
    return Current_Date
def todaystring():
    return Current_Date_String
def monthyear():
    return MonthYear

def yearstring():
    return Year
def yearint():
    return YearInt

def monthstring():
    return Month
def monthint():
    return MonthInt

def daystring():
    return Day
def dayint():
    return DayInt




if __name__ == "__main__":  # This crazy sh*t ensures you can run the program directly here or call it
    print(fulldate())
    print(yearint())
    print(monthint())
    print(dayint())
    print(daystring())

