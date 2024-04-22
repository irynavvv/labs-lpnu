rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Enter the elements of the matrix (separated by space or newline):")
X = []
for _ in range(rows):
    row = list(map(int, input().split(" ")))
    X.append(row)

print("\nInitial Matrix X:")
for row in X:
    print("\t".join(map(str, row)))

min_element = float('inf')
min_row_index = 0
min_col_index = 0

for i in range(len(X)):
    for j in range(len(X[0])):
        if X[i][j] < min_element:
            min_element = X[i][j]
            min_row_index = i
            min_col_index = j

for i in range(len(X)):
    X[i][min_col_index] = 0

for j in range(len(X[0])):
    X[min_row_index][j] = 0

print("\nMatrix X with zeros in the row and column of the minimum element:")
for row in X:
    print("\t".join(map(str, row)))
