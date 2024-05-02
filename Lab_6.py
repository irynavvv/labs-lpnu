input_string = input("Введіть рядок: ")
SZ = ''
L = True

for char in input_string:
    if char in ['+', '-', '*', '/']:
        SZ += char
        L = False

print("SZ =", SZ)
print("L =", L)