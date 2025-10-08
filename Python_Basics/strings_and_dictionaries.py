x = "Pluto is a planet"
y = 'Pluto is a planet'
x = y

print("Pluto's a planet")
print('My dog is named "Pluto"')
print('Pluto\'s a planet')
print("Look, a mountain: /\\")
print("1\n2 3")

hello = "hello\nworld"
print(hello)

triplequoted_hello = """hello
world"""
print(triplequoted_hello)

print("hello")
print("world")
print("hello", end='')
print("pluto")

planet = 'Pluto'
print(planet[0])
print(planet[-3:])
print(len(planet))

print([char+'! ' for char in planet])

claim = "Pluto is a planet"

print(claim.upper())
print(claim.lower())
print(claim.index('plan'))
print(claim.startswith(planet))

words = claim.split()
print(words)

datestr = '1956-01-31'
year , month , day = datestr.split('-')
print('/'.join([month, day, year]))

print(' $ '.join([word.upper() for word in words]))

print(planet + ', we miss you.')

position = 9
print(planet + ", you'll always be the " + str(position) + "th planet to me.")

print("{}, you'll always be the {}th planet to me.".format(planet,position))


pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390

print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(planet, pluto_mass, pluto_mass / earth_mass, population,))


s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)


"""
                       DICTIONARIES
"""

numbers = {'one':1, 'two':2, 'three':3}
print(numbers['one'])
numbers['eleven'] = 11
print(numbers)
numbers['one'] = 'Pluto'
print(numbers)

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupyter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)


for k in numbers:
    print("{} = {}".format(k, numbers[k]))

print(' '.join(sorted(planet_to_initial.values())))

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))



