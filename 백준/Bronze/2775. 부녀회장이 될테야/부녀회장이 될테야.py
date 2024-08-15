T = int(input())
k = []
n = []
sum = []
family = []
num = 0
for i in range(T):
  a = int(input())
  b = int(input())
  k.append(a)
  n.append(b)

for i in range(T):
  sum = []
  num = 0
  for j in range(n[i]):
    num += j+1
    sum.append(num)
  num = 0
  for h in range(k[i]*n[i]-n[i]):
    if sum[h] == 1:
      num = 0

    num += sum[h]
    sum.append(num)
  
  family.append(sum[k[i]*n[i]-1])

for i in family:
  print(i)