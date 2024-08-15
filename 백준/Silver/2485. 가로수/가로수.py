import math

N = int(input())
light = []
for i in range(N):
  light.append(int(input()))

inter = light[2] - light[1]

for i in range(N-1):
  n =light[i+1]-light[i]
  Interval = math.gcd(inter,n)
  inter = Interval

num = (light[-1] - light[0])//Interval + 1
print(num-N)
