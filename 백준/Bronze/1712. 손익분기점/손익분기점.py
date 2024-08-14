A,B,C = map(int,input().split())
i = 0

if C <= B:
  print(-1)
else:
  print(int(A/(C-B)+1))
