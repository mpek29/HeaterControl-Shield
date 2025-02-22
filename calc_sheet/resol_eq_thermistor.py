import numpy as np

# Coefficients des équations
A = np.array([[-1.06, 1], [0.7, 1]])

# Constantes
B = np.array([0, 3.3])

# Résolution du système
solution = np.linalg.solve(A, B)

# Extraction des solutions
x, y = solution

# Affichage des résultats
print(f"Solution: x = {x}, y = {y}")

x = 1.9
y = 2.0

# Vérification des résultats
eq1 = -1.06 * x + y
eq2 = 0.7 * x + y

print("Vérification:")
print(f"-0.5x + y = {eq1} (doit être 0)")
print(f"0.99x + y = {eq2} (doit être 3.3)")
