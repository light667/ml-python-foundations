import numpy as np

A = np.zeros((3,2))
B = np.zeros((3,2))
print(A)
print(B)

# associer les deux tableau horizontalement et verticalement

C = np.hstack((A, B))
print(C.shape)
D = np.vstack((A, B))
print(D)
print(D.shape)

E = np.concatenate((A, B), axis= 1)  # axis = 0 pour vertical et axis = 1 pour horizontal
print(E)

# methode reshape : redimensionner un tableau

D = D.reshape((3, 4))
print(D)

A = np.array([1, 2, 3])
print(A)
A = A.reshape((A.shape[0], 1))
print(A.shape)
print(A)