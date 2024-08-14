from collections import deque
N = int(input())
num = deque()
for i in range(N):
  num.append(i+1)

def card():
  num.popleft()
  num.append(num.popleft())

for i in range(N-1):
  card()

print(num[0])
  