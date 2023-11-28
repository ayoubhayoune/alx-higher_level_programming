#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lt_dg = number - (10 * int(number / 10))
if lt_dg > 5:
    print("Last digit of", number, "is", lt_dg, "and is greater than 5")
elif lt_dg == 0:
    print("Last digit of", number, "is", lt_dg, "and is 0")
elif lt_dg < 6:
    print("Last digit of", number, "is", lt_dg, "and is less than 6 and not 0")
