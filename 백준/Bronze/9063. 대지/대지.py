N = int(input())

area = 0

dotx = []
doty = []

for i in range(N):
  a,b = map(int, input().split())
  dotx.append(a)
  doty.append(b)

if N < 2:
  print(area)
else:
  width = max(dotx) - min(dotx)
  length = max(doty) - min(doty)

  print(width*length)
