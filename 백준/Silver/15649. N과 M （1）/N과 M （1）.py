#백준 15649번 N과 M(1)
from itertools import permutations

N,M = map(int,input().split())

result = list(permutations(range(1,N+1),M))
for i in result:
  for j in i:
    print(j,end = ' ')
  print()
