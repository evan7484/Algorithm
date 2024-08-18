# 백준 11659번 구간 합 구하기 4

N, M = map(int,input().split())
num = list(map(int,input().split()))

ssum = [0]
n = 0
for i in num:
  n += i
  ssum.append(n)

for a in range(M):
  i,j = map(int,input().split())
  print(ssum[j] - ssum[i-1])