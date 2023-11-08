import time
import requests


seed = 1
counter = 0

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
    time.sleep(1)
    seed += 1
    x = seed
    print(f"YOUR CURRENT NUMBER IS: {x}")
    while x != 4:
        result = odd_even_check(x)
        if result is True:
            x = int(even(x))
        else:
            x = int(odd(x))
    counter += 1