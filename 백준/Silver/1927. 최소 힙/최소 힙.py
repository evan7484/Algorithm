#백준 1927번 최소 힙

import heapq

heap = []
result = []
N = int(input())
for i in range(N):
  x = int(input())
  if x == 0:
    if heap:
      result.append(heapq.heappop(heap))
    else:
      result.append(0)
  else:
    heapq.heappush(heap,x)

for i in result:
  print(i)