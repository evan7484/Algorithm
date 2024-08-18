round = list(map(int,input().split()))
round.sort()

if round[0] + round[1] > round[2]:
  print(round[0] + round[1] + round[2])
else:
  print((round[0]+round[1])*2 -1)

