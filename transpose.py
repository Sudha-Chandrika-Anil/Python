def transpose_matrix(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

matrix=[]
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
print(f"Enter the matrix ({rows}x{cols}) row by row:")
for i in range(rows):
    row = input(f"Enter row {i+1} (space-separated values): ").split()
    row = [int(x) for x in row]
    if len(row) != cols:
        raise ValueError(f"Row {i+1} does not have {cols} columns.")
    matrix.append(row)

transposed_matrix = transpose_matrix(matrix)

print("Transposed matrix:")
for row in transposed_matrix:
    print(row)
