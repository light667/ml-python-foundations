x = True
print(x)
print(type(x))

def can_run_for_president(age):
    return age >= 35
print("Can a 19-year-old run for president?", can_run_for_president(19))
print("Can a 45-year-old run for president?", can_run_for_president(45))

def is_odd(n):
    return (n % 2) == 1
print("Is 100 odd?", is_odd(100))
print("Is -1 odd?", is_odd(-1))

def can_run_for_president(age, is_natural_born_citizen):
    return is_natural_born_citizen and (age >= 35)
print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))

def inspect(x):
    if x == 0:
        print(x, "is Zéro")
    elif x < 0 :
        print(x, "is negative")
    elif x > 0 :
        print(x, "is positive")
    else:
        print(x, "is unlike anything I've ever seen...")

inspect(0)
inspect(-15)

print(bool(1))
print(bool(0))
print(bool("asf"))
print(bool(""))

if 0 :
    print(0)
elif "spam":
    print("spam")