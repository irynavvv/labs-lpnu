import math
y = float()
print('Please enter value for X\n')
x = float(input())
if x <= 1:
    y = -math.sqrt(1-x)
    print('Result is Y= ', y, '\n')
else:
    print("ERROR: x value should be less than or equal to 1")

