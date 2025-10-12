import numpy as np

A = np.array([1, 2, 3])
print(A)
print(A.shape)
print(A.size)

# la methode .zeros qui initialise notre tableau avec des zeros , il suffit de preciser le shape (3, 2) pour un tableau a 3 ligne et 2 colonnes

B = np.zeros((3, 2))
print(B)
print(B.ndim)
print(B.shape)

# initialiser un tableau avec des 1 :

C = np.ones((3, 4))
print(C)
print(C.size)

# initialiser un tableau avec un chiffre quelconque :

D = np.full((2, 3), 9)
print(D)

# initialiser un tableau avec des nombre aleatoire

E = np.random.randn(3, 4)
print(E)