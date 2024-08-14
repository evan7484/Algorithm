n=1000
a = [False,False] + [True]*(n-1)
primes=[]
num = 0

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False

N = int(input())

prime = list(map(int,input().split()))
for i in range(N):
  if prime[i] in primes:
    num += 1

print(num)
