n,m = map(int,input().split())
tree = list(map(int,input().split()))

start = 1
end = max(tree)
result = (start+end)//2

while(start<=end):
  N = 0
  for i in tree:
    if i > result:
      N += i - result
  
  if N > m:
    start = result + 1
    result = (start+end)//2
  elif N < m:
    end = result - 1
    result = (start+end)//2
  else:
    break

print(result) 
