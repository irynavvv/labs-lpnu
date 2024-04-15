import math
x=y=float();
A=B=dx=float();
i=k=int()
print('Please enter value for start A\n');
A=float(input());
print('Please enter value for finish B\n')
B=float(input());
print('Please enter value for step Dx\n')
dx=float(input());
k=math.trunc((B-A)/dx)+1;
x=A; 
for i in range (0,k,1):
    y= 2 * math.sin(2 * x);
    print(f'x={x:10.3f} y={y:10.3f}');
    x=x+dx