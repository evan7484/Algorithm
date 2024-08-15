N = int(input())
num3 = 0
num5 = 0

for i in range(1000):
  if N < 0:
    print(-1)
    break
  elif N == 0:
    print(num3)
    break
    
  if N%5 == 0:
    num5 = N//5
    print(num3+num5)
    break
  else:
    N -= 3
    num3 += 1