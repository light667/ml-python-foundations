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

