N,M = map(int, input().split())
B = [0]*100
for a in range(M):
  i,j,k = map(int,input().split())
  for b in range(i-1,j):
    B[b] = k

for i in range(N):
  print(B[i],end = ' ')

  