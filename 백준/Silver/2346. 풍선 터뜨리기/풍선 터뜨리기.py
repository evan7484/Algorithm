# 1 2 3 4 5
# 3 2 1-3-1

from collections import deque

n = 0
def defineN():
  n = paper[num[0]-1]*-1
  if n < 0:
    n += 1
  return n

N = int(input())
paper = list(map(int,input().split()))
result = []

num = deque()
for i in range(N):
  num.append(i+1)

n = defineN()
for i in range(N-1):  
  if i == 0:
    result.append(num.popleft())
    num.rotate(n)
    n = defineN()
    result.append(num.popleft())
    continue
  num.rotate(n)
  n = defineN()
  result.append(num.popleft())
  
for i in result:
  print(i,end = ' ')

