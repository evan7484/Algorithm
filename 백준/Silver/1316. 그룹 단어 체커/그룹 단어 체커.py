N = int(input())
group = N

for i in range(N):
  words = []
  wordS = []
  word = []
  word = list(map(str,input()))

  for i in range(len(word)):
    if word.count(word[i]) > 1:
      words.append(word[i])
  
  if len(words) == 0:
    continue
  
  wordS = set(words)
  wordS = list(wordS)
  G = group

  for k in range(len(wordS)):
    num = []
    for j in range(words.count(wordS[k])):
      num.append(word.index(wordS[k]))
      word.remove(wordS[k])
      word.insert(num[j],'1')
    
    for j in range(len(num)-1):
      if num[j+1] - num[j] != 1:
        group -= 1
        break
    if G != group:
      break

print(group)
