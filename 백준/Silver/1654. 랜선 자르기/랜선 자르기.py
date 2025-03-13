k,n = map(int,input().split())
k_length = []
for i in range(k):
  k_length.append(int(input()))

k_length.sort()
start = 1
end = max(k_length)
result = (start + end)//2

while(start <= end):
  num = 0
  for i in k_length:
    num += i//result
  if num < n:
    end = result-1
    result = (end+start)//2
  elif num >= n:
    start = result+1
    result = (start+end)//2

print(result)
