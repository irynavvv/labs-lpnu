matrix = []
file=open("Lab_7.txt", "r")
lines = file.readlines()
for line in lines:
    row = list(map(int, line.split(",")))
    matrix.append(row)
print("Original Matrix:")
for row in matrix:
    print(row)

normalized_matrix = []
for row in matrix:
    max_row_value = max(row)
    normalized_row = [value / max_row_value for value in row]
    normalized_matrix.append(normalized_row)
print("\nNormalized Matrix:")
for row in normalized_matrix:
    print(row)
file.close()