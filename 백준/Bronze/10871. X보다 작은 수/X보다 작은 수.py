n,X = map(int,input().split())
list2 = []
x = list(map(int,input().split()))

for i in range(0,n):
  if (X > x[i]):
    list2.append(x[i])
  else:
    pass

for i in list2:
  print(i,end=' ')