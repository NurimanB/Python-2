import numpy as np
import pandas as pd
from numpy.linalg import det, eig

matrix_df = pd.read_csv('D:\VsCode\python-2\week 12\Matrix_Dataset.csv', header=None)

matrix = matrix_df.to_numpy()

matrix_transpose = matrix.T

matrix_determinant = det(matrix)

matrix_eigenvalues = eig(matrix)[0]

print("Matrix Transpose:\n", matrix_transpose)
print("\nMatrix Determinant:", matrix_determinant)
print("\nMatrix Eigenvalues:\n", matrix_eigenvalues)
