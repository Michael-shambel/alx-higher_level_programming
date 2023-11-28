#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lD = abs(number) % 10
if number < 0:
    lD = lD * -1
else:
    lD = lD

print(f"Last digit of {number} is {lD} and is ", end="")

if lD > 5:
    print("greater than 5")
elif lD == 0:
    print("0")
else:
    print("less than 6 and not 0")
