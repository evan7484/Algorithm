#덱
import sys
from collections import deque
num = deque()

N = int(input())
for i in range(N):
  number = list(map(int, sys.stdin.readline().strip().split()))

  if number[0] == 1:
    num.appendleft(number[1])
  elif number[0] == 2:
    num.append(number[1])
  elif number[0] == 3:
    if num:
      print(num.popleft())
    else:
      print(-1)
  elif number[0] == 4:
    if num:
      print(num.pop())
    else:
      print(-1)
  elif number[0] == 5:
    print(len(num))
  elif number[0] == 6:
    if num:
      print(0)
    else:
      print(1)
  elif number[0] == 7:
    if num:
      print(num[0])
    else:
      print(-1)
  elif number[0] == 8:
    if num:
      print(num[-1])
    else:
      print(-1)
