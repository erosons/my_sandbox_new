from sympy import Matrix, symbols, sqrt
from math import sqrt

# Define the symbol for lambda
λ = symbols('λ')

# Define your matrix A (without λ, as we will substitute eigenvalues)
B = Matrix([
[1,0,0,1,0,0,0,0,0,1,0],
[0,1,0,0,1,0,0,0,0,0,1],
[0,0,1,0,0,0,1,0,0,0,0],
[1,0,0,2,0,0,0,0,0,1,0],
[0,1,0,0,2,0,0,0,1,0,1],
[0,0,0,0,0,1,0,1,0,0,0],
[0,0,1,0,0,0,1,0,0,0,0],
[0,0,0,0,0,1,0,1,0,0,0],
[0,0,0,0,1,0,0,0,1,0,0],
[1,0,0,1,0,0,0,0,0,1,0],
[0,1,0,0,1,0,0,0,0,0,1]
])

# Compute the eigenvectors for each eigenvalue
eigenvalues=[0,2,2-sqrt(2),2+sqrt(2),5/2-sqrt(5)/2,5/2+sqrt(5)/2]
eigenvectors = []
for ev in eigenvalues:
    # Substitute the eigenvalue into the matrix
    eigenmatrix = B - ev * Matrix.eye(11)
    # Compute the eigenvectors
    eigenvectors.append(eigenmatrix.nullspace())

# eigenvectors will contain the eigenvectors for each eigenvalue
eigenvectors