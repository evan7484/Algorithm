X = int(input())
u = 0
d = 0
j = 0
while (X>0):
  j+=1
  X -=j
X += j
if j%2 == 1:
  u = j
  d = 1
  for i in range(X-1):
    u -= 1
    d += 1
  print('{}/{}'.format(u,d))
else: 
  u = 1
  d = j
  for i in range(X-1):
    u += 1
    d -= 1
  print('{}/{}'.format(u,d))