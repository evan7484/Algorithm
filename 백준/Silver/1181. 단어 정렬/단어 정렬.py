import operator

n = int(input())
wordL = {}
wordL1 = {}

for i in range(n):
  word = input()
  wordL[word] = len(word)

wordL1 = sorted(wordL.items())
wordL = sorted(dict(wordL1).items(), key=operator.itemgetter(1))

for i in range(len(wordL)):
  print(wordL[i][0])