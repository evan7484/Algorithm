from itertools import combinations

n = int(input())
array = list(map(int,input().split()))
x = int(input())

result = 0
array.sort()
start = 0; end = n-1;
while start != end:
  sum = array[start] + array[end]
  if sum > x:
    end -= 1
  else: 
    start += 1
  
  if sum == x:
    result += 1

print(result)
