import time

x = int(input("Please enter a number: "))

def even(x):
    x = x // 2
    return x

def odd(x):
    x = (3 * x) + 1
    return x

def odd_even_check(x):
    even = False
    r = x % 2
    if r == 0:
        even = True
    return even


while True:
    print(x)
    result = odd_even_check(x)
    if result is True:
        x = int(even(x))
    else:
        x = int(odd(x))
    print(f"YOUR CURRENT NUMBER IS: {x}")
    #time.sleep(1)