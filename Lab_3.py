import math
K=3
L=0.027
x=y=a=b=float()
x_values = [1, 0.329, 1.141]
print('Please enter value for X\n');
x = float(input());
a = K * math.sin(x) + math.cos(x)
print('Result is A=', a, '\n');
b = (L ** (-1/3) - (x / 6) ** (-2)) * math.log(K)
print('Result is B=', b, '\n');
if a + b < 2:
    y = math.log10(abs(a - 2*b))
elif a + b >= 2:
    y = math.log(abs(a - b*a))
print('Result is Y= ', y, '\n');
  


