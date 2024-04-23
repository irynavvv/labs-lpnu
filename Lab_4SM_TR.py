import math
x=y=float();
A=B=dx=float();
print('Please enter value for start A\n');
A=float(input());
print('Please enter value for finish B\n')
B=float(input());
print('Please enter value for step Dx\n')
dx=float(input());
x=A;
while True:
    y=math.sqrt(math.exp(x))/math.sqrt((math.exp(x)+math.exp(-x)/2))
    print(f'x={x:10.3f} y={y:10.3f}');
    x=x+dx
    if x>B:
        break;