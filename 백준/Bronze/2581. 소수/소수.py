n=10000
a = [False,False] + [True]*(n-1)
primes=[]
num = 0

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

M = int(input())
N = int(input())
prime = []
sum = 0
for i in primes:
  if M <= i <= N:
    prime.append(i)

for i in prime:
  sum += i

if len(prime) == 0:
  print(-1)
else:
  print(sum) 
  print(prime[0])