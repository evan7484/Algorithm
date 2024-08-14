from collections import Counter
import sys

input = sys.stdin.readline

Nn = int(input())
Number = []

for i in range(Nn):
  Number.append(int(input()))

Average = sum(Number)/Nn

Number.sort()
Middle = Number[Nn//2]

Mode = 0
cnt = Counter(Number)
if Nn == 1:
  Mode = Number[0]
else:
  mode = cnt.most_common(2)
  if mode[0][1] == mode[1][1]:
    Mode = mode[1][0]
  else: 
    Mode = mode[0][0]

Range = Number[-1] - Number[0]

print(round(Average))
print(Middle)
print(Mode)
print(Range)
