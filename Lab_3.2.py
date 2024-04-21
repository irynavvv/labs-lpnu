import math

K = 3
L = 0.027
x = y = a = b = float()
x_values = [1, 0.329, 1.141]
print('Please enter value for X\n')
x = float(input())
a = K * math.sin(x) + math.cos(x)
print('Result is A=', a, '\n')
b = (L ** (-1 / 3) - (x / 6) ** (-2)) * math.log(K)
print('Result is B=', b, '\n')

if a + b < 2:
    val = a - 2 * b
    if val == 0:
        print("ERROR: log value cannot be equal to 0")
    else:
        y = math.log10(abs(val))
elif a + b >= 2:
    val = a - b * a
    if val == 0:
        print("ERROR: log value cannot be equal to 0")
    else:
        y = math.log(abs(val))
print('Result is Y= ', y, '\n')
