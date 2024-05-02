input_string = input("Введіть рядок: ")
input_string = input_string.strip().replace(" ", "")
SZ = ''.join(char for char in input_string if char in ['+', '-', '*', '/'])
if not SZ.strip():
    L = True
    print("L =", L)
else:
    print("SZ =", SZ)