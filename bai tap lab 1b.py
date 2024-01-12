a = float(input("type_a:"))
b = float(input("type_b:"))
c = float(input("type_c:"))
x = float(input("type_x:"))
import math
S1 = a * x**3 + b*x + c
print("value of S1:",S1)
D = b**2 - 4*a*c
if D > 0:
    S2 = math.sqrt(D)
else:
    S2=0
print("value of S2:",S2)
if (a + b <= c) or (a + c <= b):
    print("a,b,c is not a side of a triangle")
else:
    print("a,b,c is a side of a triangle")
    p=(a+b+c)/2
    S3 = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("The area of a triangle a,b,c: ",S3)
