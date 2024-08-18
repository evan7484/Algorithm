#백준 15652번 N과 M(4)
from itertools import *

N,M = map(int,input().split())

result = list(combinations_with_replacement(range(1,N+1),M))

for i in result:
  for j in i:
    print(j,end = ' ')
  print()
