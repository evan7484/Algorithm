T = int(input())
rest = []

for i in range(T):
  C = int(input())
  rest.append(C//25)
  C = C%25
  rest.append(C//10)
  C = C%10
  rest.append(C//5)
  C = C%5
  rest.append(C)

for i in range(0,len(rest),4):
  print(rest[i],rest[i+1],rest[i+2],rest[i+3])