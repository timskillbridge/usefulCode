import random

rand_list = [x for x in range(101)]

for x in range(100):
    r1 = random.randint(0,100)
    r2 = random.randint(0,100)
    hold = rand_list[r1]
    rand_list[r1] = r2
    rand_list[r2] = hold


"""
list of 1 - 100
random number to find

def start: lower limit
def stop: upper limit / 2

is number in between?
Yes: 
lower = lower
upper = upper /2

No:
lower = upper/2
upper = upper
"""

def find_in_list(looking_for):
    rand_list = [str(x) for x in range(101)]

    for x in range(100):
        r1 = random.randint(0,100)
        r2 = random.randint(0,100)
        hold = rand_list[r1]
        rand_list[r1] = r2
        rand_list[r2] = hold


    start = 0
    stop = 100
    current = str(rand_list[stop])
    while current != looking_for:
        if looking_for in rand_list[start:int(stop/2)]:
            print(rand_list[start:stop+1])
            stop = int(stop/2)
            current = str(rand_list[stop])
        elif looking_for not in rand_list[start:int(stop/2)]:
            start = int(stop/2)
            current = str(rand_list[start])
        print(f"somewhere in between {start} and {stop}")
    print( f"found it, current: {current} = looking: {looking_for}")

find_in_list('45')