#1 6 12 18 24 30 36....
N = int(input())
n = 1
for i in range(1,1000000000):
  
  if N <= n:
    print(i) 
    break

  n += (6 * i)





