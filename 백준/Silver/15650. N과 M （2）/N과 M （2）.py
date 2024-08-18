# 백준 15650번 N과 M(2)
from itertools import combinations

N,M = map(int,input().split())

result = list(combinations(range(1,N+1),M))
for i in result:
  for j in i:
    print(j,end = ' ')
  print()

