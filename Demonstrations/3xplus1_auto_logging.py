import time

try:
    with open("Counter_Log.txt", "r+") as file:
        seed = file.readlines()
        seed = int(seed[0])
        print(f"Left off at {seed}!!!")
        time.sleep(5)
except FileNotFoundError:
    seed = 1


counter = 0
log_counter = 0

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
    #time.sleep(1)
    seed += 1
    x = seed
    while x != 4:
        result = odd_even_check(x)
        if result is True:
            x = int(even(x))
        else:
            x = int(odd(x))
    # counter += 1
    log_counter += 1
    if log_counter == 100000:
        print(f"LOGGING NUMBER {seed}")
        with open("Counter_Log.txt", "w") as file:
            file.write(str(seed))
            log_counter = 0