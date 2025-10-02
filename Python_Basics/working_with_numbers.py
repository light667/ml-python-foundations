# reviser les operateurs
"""
 +   addition
 -   subtraction
 *   multiplication
 /   True division
 //  Floor division
 %   Modulus
 **  Exponentiation
"""
print(5/2)
print(5//2)
print(8 - 3 + 2)
hat_height_cm = 25
my_height_cm = 190
total_height_meters = hat_height_cm + my_height_cm / 100
total_height_meters2 = (hat_height_cm + my_height_cm)/ 100
print("Height in meters = ", total_height_meters, "?")
print("My height in meters = ", total_height_meters2 ,"!")

# builtin functions for working with numbers
"""
min , max , abs , float , int 
"""
print(min(1,2,3))
print(max(1,2,3))
print(abs(-32))
print(float(10))
print(int(3.33))
print(int('807') + 1)

"""
The help() function
"""
help(round)
help(print)
print("light", sep= "*", end= ".")
