number = [0]*30
num = []
answer  = []
for i in range(30):
  number[i] = i+1

for i in range(28):
  n = int(input())
  num.append(n)

for i in number:
  if i not in num:
    answer.append(i)

print(answer[0])
print(answer[1])
