import math

print("It's math! It has type {}".format(type(math)))

print(dir(math))
print('pi to 4 significant digits = {:.4}'.format(math.pi))

print(math.log(32,2))
help(math.log)
help(math)

# import math as mt or mt = math
mt = math
print(mt.pi)

# from math import *
from math import *
print(pi, log(32, 2))
