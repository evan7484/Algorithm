num = int(input())
divisor = list(map(int,input().split()))
divisor.sort()

if len(divisor) > 1:
  print(divisor[0]*divisor[-1])
else:
  print(divisor[0]*divisor[0])
