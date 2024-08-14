# 백준 1931번 회의실 배정
# 딕셔너리도 해봐도 될듯 -> 안될듯 딕셔너리에 리스트가 안 들어감
N = int(input())
time = []
result = 0
end = []
n = 0

for i in range(N):
  a,b = map(int,input().split())
  time.append([a,b])
  end.append(b)

time.sort(key=lambda x: (x[1], x[0]))
for i in range(N):
  if n <= time[i][0]:
    n = time[i][1]
    result += 1

print(result)
