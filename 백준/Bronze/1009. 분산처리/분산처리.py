T = int(input())
result = []
b2 = [2,4,8,6]
b3 = [3,9,7,1]
b7 = [7,9,3,1]
b8 = [8,4,2,6]
for i in range(T):
  a,b = map(int, input().split())
  
  if a%10 == 0:
    data = 10
  elif a%10 == 1:
    data = 1
  elif a%10 == 2:
    if b%4 == 0:
      data = b2[3]
    data = b2[b%4-1]
  elif a%10 == 3:
    if b%4 == 0:
      data = b3[3]
    data = b3[b%4-1]
  elif a%10 == 4:
    if b%2 == 1:
      data = 4
    else:
      data = 6
  elif a%10 == 5:
    data = 5
  elif a%10 == 6:
    data = 6
  elif a%10 == 7:
    if b%4 == 0:
      data = b7[3]
    data = b7[b%4-1]
  elif a%10 == 8:
    if b%4 == 0:
      data = b8[3]
    data = b8[b%4-1]
  elif a%10 == 9:
    if b%2 == 1:
      data = 9
    else:
      data = 1
  result.append(data)
 
for i in result:
  print(i)
