n,m = map(int, input().split())
basket = []
for i in range(n):
  basket.append(i+1)


for i in range(m):
  a,b = map(int, input().split())
  if a == b:
    continue
  num = b-a+1
  N = a-1
  temp = []
  for j in range(num):
    temp.append(0)
    temp[j] = basket[a-1]
    a += 1

  temp.reverse()
  for k in range(num):
    basket[N] = temp[k]
    N += 1
for i in basket:
  print(i, end =' ')