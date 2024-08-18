# 백준 11047번 동전 0

N,K = map(int,input().split())
Money = K # K값을 저장해놓기
Coin = [] # 가지고 있는 동전의 종류
result = 0 # K원을 만드는데 필요한 동전의 개수
n = 0 # Coin의 index 역할

for i in range(N):
  Coin.append(int(input()))

Coin.sort(reverse = True) #큰 동전부터 계산할 것이므로 내림차순으로 정렬

while K != 0:
  Money = K
  K -= Coin[n]
  if K < 0: # 동전 값을 뺐을 때 음수일시 무효처리
    K = Money
    n += 1
    continue
  result += 1 # 동전 개수 세기

print(result)