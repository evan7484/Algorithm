n = 5
N = []
sum = 0

for i in range(n):
  num = int(input())
  sum += num
  N.append(num)

N.sort()
print(sum//5)
print(N[2])