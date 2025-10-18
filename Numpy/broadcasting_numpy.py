import numpy as np

A = np.random.randint(0, 10, [2, 3])
B = np.ones((2, 3))
print(A)
print(B)

print(A + B)
# le broadcasting permet d'etendre la dimension d'un tableau pour effectuer des operations

print(A + 2)

B = np.ones((2, 1))

print(A + B)
"""
B = np.ones((3, 1))
print(A + B)      il y'aura erreur parce que les dimensions different

"""
# mais si on a:

C = np.ones((4, 1))
D = np.random.randint(0, 10, [1, 3])
print(C)
print(D)
print(C + D)