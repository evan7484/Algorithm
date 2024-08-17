# 백준 10986번 나머지 합
# https://www.acmicpc.net/problem/10986
# 거의 그냥 이건 수학 문제였다
#이걸 기억하자 구간합은 누적합의 뺄셈으로 구할 수 있다.

N,M = map(int,input().split())
Num = list(map(int,input().split()))
n = 0
result = 0
remain = [0] * M

for i in range(N):
  n += Num[i]
  remain[n%M] += 1

result += remain[0]
for i in range(M):
  result += (remain[i] * (remain[i]-1))//2

print(result)