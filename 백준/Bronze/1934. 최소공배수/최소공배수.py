#최소공배수 함수 math.lcm
#최대공약수 함수 math.gcd
import math
T = int(input())
results = []

for i in range(T):
  A,B = map(int,input().split())

  results.append(math.lcm(A,B))

for i in results:
   print(i)
