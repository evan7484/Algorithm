#백준 15651번 N과 M(3)
from itertools import *

N,M = map(int,input().split())

result = list(product(range(1,N+1),repeat = M))

for i in result:
  for j in i:
    print(j,end = ' ')
  print()
