n= 300000
a = [False,False] + [True]*(n-1)
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

prime = []
num = []
N = int(input())
while N != 0:
  for i in primes:
    if N < i <= 2*N:
      prime.append(i)
  num.append(len(prime))
  prime = []
  N = int(input())

for i in num:
  print(i)
