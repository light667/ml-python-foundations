import fonctions_exo  as ft

liste = ft.fibonacci(50)
print(liste)

from fonctions_exo import fibonacci

liste2 = fibonacci(60)
print(liste2)

import math
import random
import statistics
import os
import glob

"""
            MATH
"""
print(math.cos(2*math.pi))
print(math.exp(5))

"""
            STATISTICS
"""

print(statistics.mean(liste))
print(statistics.variance(liste))

"""
          RANDOM
"""
random.seed(3)
print(random.choice(liste))
print(random.choice(["julie","jean","jacques"]))

print(random.random())  # float
print(random.randint(5,10))  #int
print(random.randrange(100))  # int entre 0 et 100

# generer une liste aléatoire
print(random.sample(range(100), 3))
print(random.sample(range(100), random.randrange(10)))

print(random.shuffle(liste))


"""
          OS 
"""

print(os.getcwd())



"""
        GLOB
"""
print(glob.glob("*"))

"""filenames = glob.glob('*.txt')

for file in filenames:
    with open(file, 'r') as f:
        print(f.read())
"""
with open('villes.txt', 'r') as f:
    liste = f.read().splitlines()
print(liste)