import math

a,A = map(int,input().split())
b,B = map(int,input().split())

R = math.lcm(A,B)
a = a*(R//A)
b = b*(R//B)
r = a+b
n = math.gcd(r,R)
if  n != 1:
  r = r//n
  R = R//n

print(r,R)