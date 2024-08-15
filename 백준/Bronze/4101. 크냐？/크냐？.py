#4101번 크냐?

a = 1
b = 1
result = []
while 1:
  a,b = map(int,input().split())
  if a == 0 and b == 0:
    break
  if a > b:
    result.append('Yes')
  else:
    result.append('No')

for i in result:
  print(i)
    