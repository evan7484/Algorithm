#7,3 요세푸스 순열
#1 2 3 4 5 6 7
#3 6 2 7 5 1 4
from collections import deque
num = deque()

N, K = map(int,input().split())
result = []
for i in range(N):
  num.append(i+1)

for i in range(N):
  num.rotate((K-1)*-1)
  result.append(num.popleft())
  
print('<',end = '')
for i in range(len(result)):
  if i == len(result)-1:
    print(str(result[i])+'>')
  else:
    print(str(result[i])+',',end = ' ')