# 백준 1453번 피시방 알바
# https://www.acmicpc.net/problem/1453

N = int(input())
want = list(map(int,input().split()))
result = []
n = 0

for i in range(N):
  if want[i] not in result:
    result.append(want[i])
  else:
    n += 1
print(n)