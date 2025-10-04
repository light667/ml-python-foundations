planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets :
    print(planet)

multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
print(product)

s = 'steganograpHy is the praticE of concealing a fiLe, message, image or video within another fiLe, message, image, Or video '
msg = ''
for char in s:
    if char.isupper():
        print(char, end='')


for i in range(5):
    print("Doing important work. i = ", i)

i = 0
while i < 10:
    print(i, end=' ')
    i += 1

square = [n**2 for n in range(10)]
print(square)

square = []
for n in range(10):
    square.append(n**2)
print(square)

short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)

loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
print(loud_short_planets)

def count_negatives(nums):
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative