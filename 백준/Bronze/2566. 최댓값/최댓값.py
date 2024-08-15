max = 0
A = [[0 for j in range(9)] for i in range(9)]
a = 0
b = 0

for i in range(9):
  A[i] = list(map(int,input().split()))

for i in range(9):
  for j in range(9):
    if max < A[i][j]:
      max = A[i][j]
      a = i
      b = j

print(max)
print(a+1,b+1)
