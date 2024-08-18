N, M = map(int, input().split())
basket = []

for i in range(N):
  basket.append(i+1)

for a in range(M):
  i,j,k = map(int,input().split())
  for b in range(i,k):
    basket.insert(j,basket[i-1])
    del basket[i-1]
    
 # for c in basket:
    #print(c, end = " ")

for i in basket:
  print(i, end = " ")
