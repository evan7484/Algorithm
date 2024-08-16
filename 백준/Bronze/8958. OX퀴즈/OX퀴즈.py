num = int(input())
score = 0
test = 0
n = 0
for i in range(num):
  answer = list(map(str,input()))
  for i in range(len(answer)):
    if answer[i] == 'O':
      test +=(n+1)
      n+=1
    elif answer[i] == 'X':
      score += test
      test = 0
      n = 0
  if answer[-1] == 'O':
    score += test
    test = 0
    n = 0
  
  answer = []
  print(score)
  score = 0


  