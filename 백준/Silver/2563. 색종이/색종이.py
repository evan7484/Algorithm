N = int(input())
A = [[0 for j in range(100)] for i in range(100)]
B = [[0 for j in range(2)] for i in range(N)]
sum = 0

for i in range(N):
  B[i] = list(map(int,input().split()))

for i in range(100):
  for j in range(100):
    A[i][j] = 0

for i in range(N):
  for j in range(B[i][0],B[i][0]+10):
    for k in range(B[i][1],B[i][1]+10):
      A[j][k] = 1

for i in range(100):
  for j in range(100):
    sum += A[i][j]
    
print(sum)