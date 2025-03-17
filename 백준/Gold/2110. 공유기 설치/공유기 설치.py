n,c = map(int,input().split()) #감사합니다~
coordinate = []
for i in range(n):
  coordinate.append(int(input()))

coordinate.sort()
start = 1
end = coordinate[-1] - coordinate[0]
result = 0

while(start <= end):
  mid = (start+end)//2
  cnt = 1
  tmp = coordinate[0]

  for i in range(1,n):  
    if mid <= coordinate[i]-tmp:
      cnt += 1
      tmp = coordinate[i]
  
  if cnt < c:
    end = mid-1
  else:
    result = mid
    start = mid+1

print(result)