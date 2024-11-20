import numpy as np

matrix_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix_2 = np.array([[1,3,5],[6,8,0],[2,4,7]])

addition = np.add(matrix_1,matrix_2)
substraction = np.subtract(matrix_1,matrix_2)
multiplication = np.multiply(matrix_1,matrix_2)

print('Addition:/n', addition)
print('Substraction:/n', substraction)
print('Multiplication:/n', multiplication)
