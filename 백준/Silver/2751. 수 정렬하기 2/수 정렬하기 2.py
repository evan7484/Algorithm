n = int(input())
N = []

for i in range(n):
  num = int(input())
  N.append(num)

N.sort()

for i in N:
  print(i)