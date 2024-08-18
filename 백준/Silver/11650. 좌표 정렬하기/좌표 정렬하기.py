n = int(input())
lis = []

for i in range(n):
  a,b = map(int, input().split())
  lis.append([a,b])

lis.sort()
for i in range(n):
  for j in lis[i]:
    print(j,'' ,end = '')
  print(sep = '\n')
