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

def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    result = []
    for i in range(rows):
        result_row = []
        for j in range(cols):
            result_row.append(matrix1[i][j] + matrix2[i][j])
        result.append(result_row)
    return result

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Matrix 1:")
matrix1 = input_matrix(rows, cols)

print("Matrix 2:")
matrix2 = input_matrix(rows, cols)

try:
    result_matrix = add_matrices(matrix1, matrix2)
    print("The result of matrix addition is:")
    print_matrix(result_matrix)
except ValueError as e:
    print(f"Error: {e}")
