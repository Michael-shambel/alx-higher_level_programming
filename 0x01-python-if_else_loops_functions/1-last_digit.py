#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lD = abs(number) % 10
if number < 0:
    lD = lD * -1
else:
    lD = lD

if lD > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, lD))
elif lD == 0:
    print("Last digit of {} is {} and is 0".format(number,ld))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,lD))
