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

# pour fixer le resultat on utilisera :
np.random.seed(123)
E = np.random.randn(3, 4)
print(E)

# creer une matrice identité
F = np.eye(4)
print(F)

# creer un tableau a 1 dimension avec un debut , une fin , et le nombre d'element qu'elle va contenire de facons egal

G = np.linspace(0, 10, 5)
print(G)

# creer un tableau avec un debut , une fin et le pas
H = np.arange(0, 10, 1)
print(H)
