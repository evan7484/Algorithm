n=1000000
a = [False,False] + [True]*(n-1)
primes=[]
num = 0

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

M ,N = map(int,input().split())
prime = []

for i in primes:
  if M <= i <= N:
    prime.append(i)

for i in prime:
  print(i)