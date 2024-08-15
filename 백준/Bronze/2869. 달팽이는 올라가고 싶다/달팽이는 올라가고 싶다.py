import math
A, B, V = map(int,input().split())
i = 0

N = A-B
D = (V-A)/N


if 1 > D > 0:
  D = 1

print(math.ceil(D+1))
