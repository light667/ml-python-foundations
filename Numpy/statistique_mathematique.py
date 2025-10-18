import numpy as np

A = np.random.randint(0, 10, [5, 5])
print(A)


# methodes ndarray

print(A.sum())
# somme suivant les axes
print(A.sum(axis=0)) # vertical : colonne

print(A.sum(axis=1)) # horizontal : ligne

# somme cumulé 
print(A.cumsum())
# suivant l'axe 0
print(A.cumsum(axis=0))

# produit
print(A.prod())
# produit cumulé
print(A.cumprod())
# produit cumulé suivant l'axe 1
print(A.cumprod(axis=1))

# minimum et maximum
print(A.min())
print(A.max())

# minimum suivant l'axe 0
print(A.min(axis=0))

# trouver la position du minimum
print(A.argmin(axis=0))

# retourner la façon dont faut placer les index afin de trier notre tableau soit du plus grand au plus petit soit du plus petit au plus grand

print(A.argsort(axis=1))


# fonctions ndarray

print(np.exp(A))
print(np.log(A))
print(np.sin(A))


"""
          STATISTIQUES AVEC Numpy
"""

# on suppose qu'il y'a une dataset A qui vient d'arriver , on cherche premierement le min et max

print(A.min())
# la moyenne du tableau et la moyenne suivant un axe

print(A.mean())
print(A.mean(axis=0))
# l'ecart-type du tableau
print(A.std())
# la variance
print(A.var())

# tracer une matrice de coorelation entre les differentes lignes ou colonnes du tableau
print(np.corrcoef(A))
# pour avoir le coefficient de coorelation de la ligne 1 avec la ligne 2 par exemple :

print(np.corrcoef(A)[0, 1])

# trouver le nombre de fois qu'un element se repete
print(np.unique(A, return_counts= True))

values , counts = np.unique(A, return_counts= True)
print(counts.argsort())
print(values[counts.argsort()])

for i , j in zip(values[counts.argsort()], counts[counts.argsort()]):
    print(f'valeur {i} apparait {j}')


"""
            NAN Corrections : Not A Number
"""

A = np.random.randn(5, 5)
A[0, 2] = np.nan
A[4, 3] = np.nan
print(A)

print(A.mean())   # on obtient nan
# pour eviter ça on fait 
print(np.nanmean(A))
print(np.nanvar(A))

# comment compter le nombre de fois qu'on a un nan dans un tableau : la fonction isnan
print(np.isnan(A))
print(np.isnan(A).sum())
print(np.isnan(A).sum()/ A.size)     # connaitre le pourcentage des nan dans le tableau

# se debarasser des nan dans un tableau
A[np.isnan(A)] = 0
print(A)



"""
                  ALGEBRE LINEAIRE
"""

A = np.ones((2, 3))
B = np.ones((3, 2))

# transposer la matrice A
print(A.T)

# produit matricielle
print(A.dot(B))
print(B.dot(A))

# calculer le determinant
print(np.linalg.det(A))

# inverser la matrice A
print(np.linalg.inv(A))

# trouver les valeurs propores ert les vecteurs propres
print(np.linalg.eig(A))