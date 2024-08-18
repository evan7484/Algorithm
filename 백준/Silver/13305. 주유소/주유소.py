# 백준 13305번 주유소

N = int(input()) # 도시의 개수
Distance = list(map(int,input().split())) # 거리마다 kn수
Price = list(map(int,input().split())) # 기름의 가격
Min = Price[0] # 기름 최소 가격
result = 0 # 최소비용

#result += Distance[0] * Price[0]
for i in range(N-1):
  if Min > Price[i]:
    Min = Price[i]
  result += Min*Distance[i]
  
print(result)