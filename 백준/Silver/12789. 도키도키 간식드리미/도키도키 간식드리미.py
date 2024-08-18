# 5 3 1 4 2
N = int(input())
Order = list(map(int,input().split()))
target = 1
Line = []

while target != N:
  if Order and Order[0] == target:
    Order.pop(0)
    target += 1
  elif Line and Line[-1] == target:
    Line.pop(-1)
    target += 1
  else:
    Line.append(Order.pop(0))
    if len(Line) > 1 and Line[-1] > Line[-2]:
      print('Sad')
      Order = [1]
      break
      
if target == N:
  print('Nice')

