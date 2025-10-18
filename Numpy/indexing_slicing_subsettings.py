import numpy as np
A = np.array([[1, 2, 3, ], [4, 5, 6], [7, 8, 9]])
print(A)
# indexing
print(A[0, 0])
print(A[1, 1])

# slicing

#   A[début:fin, debut:fin]
# imprimer toute la premiere colonne
print(A[:,0])

# imprimer toute la premiere ligne
print(A[0, :])

# imprimer la premiere ligne :
print(A[0])

# imprimer les deux premieres lignes et les deux premieres colonne
print(A[0:2, 0:2])

# Subsettings
B = A[0:2, 0:2]
print(B.shape)
A[0:2, 0:2] = 10
print(A)

C = A[:, 1:]
print(C)

D = np.zeros((4, 4))
print(D)
# remplacer les 4 element du milieu de ce tableau par la valeur 1
D[1:3, 1:3] = 1
print(D)

E = np.zeros((5, 5))
print(E)

# remplacer la premiere , troisieme et la 5eme case des lignes 1, 3, 5 par un 1
# introduction de la notion de pas

E[::2, ::2] = 1
print(E)

# BOolean indexing
F = np.random.randint(0, 10, [5, 5])
print(F)

print(F< 5)

# boolean indexing : remplacer tout les nombre superieur a 5 dans le tableau par 10
F[F< 5] = 10
print(F)

F[(F< 5) &  (F > 2)] = 15
print(F)

print(F[F< 15])


