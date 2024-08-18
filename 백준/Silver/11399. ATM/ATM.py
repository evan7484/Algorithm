# 백준 11399번 ATM

N = int(input()) # 사람 수
P = list(map(int,input().split())) # 돈을 인출하는데 걸리는 시간
result = 0 # 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값

#여기서 이 합의 최소를 구하는 방법이 시간이 가장 적게 걸리는 사람이 맨앞에 갈 수록 빨리 끝난다.

P.sort(reverse = True) # 내림차순으로 정렬 후 차례로 더하려고 한다

for i in range(N):
  result += P[i] * (i+1)

print(result)