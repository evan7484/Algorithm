w = input().upper()
words = []
for i in w:
  words.append(i)
word1 = set(words)
word = list(word1)

M = []
num = words.count(word[0])

for i in range(1,len(word)):
  if num < words.count(word[i]):
    num = words.count(word[i])

for i in range(len(word)):
  if num == words.count(word[i]):
    M.append(word[i])

if len(M) > 1:
  print('?')
else:
  print(M[0])