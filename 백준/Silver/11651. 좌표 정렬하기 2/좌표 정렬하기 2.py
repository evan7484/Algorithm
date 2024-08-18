n = int(input())
lis = []
a = 0

for i in range(n):
  a,b = map(int, input().split())
  lis.append([b,a])

lis.sort()
for i in range(n):
  a = lis[i][0]
  lis[i][0] = lis[i][1]
  lis[i][1] = a
for i in range(n):
  for j in lis[i]:
    print(j,'' ,end = '') 
  print(sep = '\n')
