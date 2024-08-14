# 백준 1049번 기타줄
# https://www.acmicpc.net/problem/1049

N,M = map(int,input().split())
six = []
one = []
result = []
price = 0
hoxy1 = 0
hoxy2 = 0
for i in range(M):
  s,o = map(int,input().split())
  six.append(s)
  one.append(o)

n = N//6
price += n * min(six)
price += (N-n*6) * min(one)
result.append(price)
hoxy1 += (n+1) * min(six)
result.append(hoxy1)
hoxy2 += N * min(one)
result.append(hoxy2)
print(min(result))
