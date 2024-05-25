import numpy as np
def input_matrix(rows, cols):
    matrix = []
    print(f"Enter the matrix ({rows}x{cols}) row by row:")
    for i in range(rows):
        row = input(f"Enter row {i+1} (space-separated values): ").split()
        row = [int(x) for x in row]
        if len(row) != cols:
            raise ValueError(f"Row {i+1} does not have {cols} columns.")
        matrix.append(row)
    return matrix

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Matrix 1:")
matrix1 = input_matrix(rows, cols)

print("Matrix 2:")
matrix2 = input_matrix(rows, cols)

res=np.dot(matrix1,matrix2)
print("Matrix Multiplication: ")
print(res)