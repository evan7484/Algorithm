length = [1,1,1]
research = []

while length[0] != 0 and length[1] != 0 and length[2] != 0:
  length = []
  length = list(map(int,input().split()))
  length.sort()

  if length[2] < length[0] + length[1]:
    if length[0] == length[1] and length[0] == length[2]:
      research.append('Equilateral')
    elif length[0] == length[1] or length[0] == length[2] or length[1] == length[2]:
      research.append('Isosceles')
    else:
      research.append('Scalene')
  else:
    research.append('Invalid')

N = len(research)
for i in range(N-1):
  print(research[i])