import numpy as np

# creating a Numpy matrix
n_array = np.array([[19, 56, 78], [67, 26, 86],[99, 45, 126]])
n_array1 = np.array([[69, 98], [56, 67]])

# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)

# calculating the determinant of matrix
det = np.linalg.det(n_array)

print("\nDeterminant of given matrix:")
print(round(det,2))