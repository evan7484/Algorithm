n,m = map(int, input().split())
basket = []
for i in range(n):
  basket.append(i+1)

for i in range(m):
  a,b = map(int, input().split())
  c = basket[a-1]
  basket[a-1] = basket[b-1]
  basket[b-1] = c

for i in basket:
  print(i, end =' ')