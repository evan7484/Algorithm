#백준 11286번 절댓값 힙

import heapq

min_heap = []
max_heap = []
result = []
N = int(input())
for i in range(N):
  x = int(input())
  if x > 0:
    heapq.heappush(min_heap, x)
  elif x < 0:
    heapq.heappush(max_heap, -x)
  else:
    if min_heap:
      if max_heap:
        if min_heap[0] < abs(max_heap[0]): 
          result.append(heapq.heappop(min_heap))
        else: 
          result.append(-heapq.heappop(max_heap))
      else: 
          result.append(heapq.heappop(min_heap))
    elif max_heap:
      result.append(-heapq.heappop(max_heap))
    else:
      result.append(0)

for i in result:
  print(i)