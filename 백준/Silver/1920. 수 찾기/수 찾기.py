# 백준 1920번 수 찾기
# 이분탐색 안 하고 그냥 in으로 찾으려 햇는데 역시 안 되네ㅋㅋ

N = int(input())
Nnum = list(map(int,input().split()))
M = int(input())
Mnum = list(map(int,input().split()))
Nnum.sort()

for i in Mnum:
  end = N-1
  start = 0
  exist = False
  while end >= start:
    mid = (start+end)//2
    if Nnum[mid] == i:
      exist = True
      print(1)
      break
    elif Nnum[mid] > i:
      end = mid-1
    else:
      start = mid+1

  if not exist:
    print(0)