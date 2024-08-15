# 백준 2559번 수열 
# https://www.acmicpc.net/problem/2559

N, K = map(int,input().split())
temp = list(map(int,input().split()))
add = 0
result = []
for i in range(K):
  add += temp[i]

result.append(add)

for i in range(N-K):
  add -= temp[i]
  add += temp[i+K]
  result.append(add)

print(max(result))