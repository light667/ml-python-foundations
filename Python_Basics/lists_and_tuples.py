# differentes types de lists
primes = [2, 3, 5, 7]
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K']
]

my_favourite_things = [32, 'raindrops on roses', help]

# Indexing

print(planets[0])
print(planets[1])
print(planets[-1])
print(planets[-2])

# Slicing

print(planets[0:3])
print(planets[:3])
print(planets[3:])
print(planets[1:-1])
print(planets[-3:])
print(planets[1:7:2])

# changing lists

planets[3] = 'Malacandra'
print(planets)

planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)

planets[:4] = ['Mercury', 'Venus', 'Earth', 'Mars']
print(planets)

# list functions

print(len(planets))
print(sorted(planets))

print(sum(primes))
print(max(primes))

# Interlude: Objects
x = 12
print(x.imag)
y = 12 + 3j
print(y.imag)
print(x.bit_length())

# List methods

planets.append('Pluto')
print(planets)

planets.pop()
print(planets)

print(planets.index('Earth'))

print("Earth" in planets)
print("Calbefraques" in planets)

# help(planets)

"""
     Tuples
"""
t = (1, 2, 3)
print(t)
t = 1, 2, 3  # equivalent to above

x = 0.125
x.as_integer_ratio() # equal to x = (1, 8)
numerator , denominator = x.as_integer_ratio()
print(numerator / denominator)

a = 1
b = 0
a, b = b, a
print(a, b)