import math

S = float()
Si = float()
y = float()
x = float()
eps = float()
A = float()
V = float()
i = j = int()

print('Enter x')
x = float(input())
print('Enter eps')
eps = float(input())

i = 1
Si = (-1) * (i) * x
S = x * Si

while math.fabs(Si) < eps:
    i = 1
    Si = Si * (-1) * (i) * x
    S = S + Si
y=math.exp((-1)*math.log(1+x));
A=math.fabs(y-S);
V=A/math.fabs(y)*100;
print(f'x{x:10.6f} eps={eps:10.6f}');
print(f'y{y:10.6f} S={S:10.6f}');
print(f'A{A:10.6f} V={V:10.6f}%')    