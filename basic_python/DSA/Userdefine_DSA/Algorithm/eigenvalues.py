
from sympy import Matrix, symbols, solve

# Define the symbol for lambda
λ = symbols('λ')

# Define your matrix A with 'λ' on the diagonal elements
A = Matrix([
[1-λ,0,0,1,0,0,0,0,0,1,0],
[0,1-λ,0,0,1,0,0,0,0,0,1],
[0,0,1-λ,0,0,0,1,0,0,0,0],
[1,0,0,2-λ,0,0,0,0,0,1,0],
[0,1,0,0,2-λ,0,0,0,1,0,1],
[0,0,0,0,0,1-λ,0,1,0,0,0],
[0,0,1,0,0,0,1-λ,0,0,0,0],
[0,0,0,0,0,1,0,1-λ,0,0,0],
[0,0,0,0,1,0,0,0,1-λ,0,0],
[1,0,0,1,0,0,0,0,0,1-λ,0],
[0,1,0,0,1,0,0,0,0,0,1-λ]
])

# Compute the characteristic polynomial
char_poly = A.charpoly(λ).as_expr()

# Solve the characteristic polynomial for eigenvalues
eigenvalues = solve(char_poly, λ)

eigenvalues
