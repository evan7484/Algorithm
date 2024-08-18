import sys
input = sys.stdin.readline

n = int(input())
num = [0]*10000

for i in range(n):
  a = int(input())
  num[a-1] += 1

for i in range(10000):
  if num[i] != 0:
    for j in range(num[i]):
      print(i+1)
