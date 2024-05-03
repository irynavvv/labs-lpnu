import random
matrix = [[random.randint(1, 100) for _ in range(8)] for _ in range(7)]
min_value = min(min(row) for row in matrix)
min_row, min_col = 0, 0
for i, row in enumerate(matrix):
    for j, value in enumerate(row):
        if value == min_value:
            min_row, min_col = i, j
            break
for i in range(7):
    matrix[i][min_col] = 0
for j in range(8):
    matrix[min_row][j] = 0
for row in matrix:
    for value in row:
        print(value, end=' ')
    print() 
