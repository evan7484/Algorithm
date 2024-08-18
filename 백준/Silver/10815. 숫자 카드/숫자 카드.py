N = int(input())
card = list(map(int,input().split()))
M = int(input())
example = list(map(int,input().split()))

dic = {}
for i in range(len(card)):
  dic[card[i]] = 0

for i in range(len(example)):
  if example[i] not in dic:
    print(0, end = ' ')
  else:
    print(1, end = ' ')