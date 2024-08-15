from itertools import combinations, permutations

N,M = map(int,input().split())
card = list(map(int,input().split()))
nC3 = list(combinations(card, 3))
max = 0

for i in range(len(nC3)):
    n = nC3[i][0]+nC3[i][1]+nC3[i][2]
    if n == M:
      max = M
      break
    elif max < n < M+1:
      max = n
print(max)
  