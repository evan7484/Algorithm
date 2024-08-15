p,q = map(int,input().split())
yaksu = []

for i in range(1,10000):
  if i > p:
    break

  if p%i == 0:
    yaksu.append(i)

if len(yaksu) < q:
  print(0)
else:
  print(yaksu[q-1])
