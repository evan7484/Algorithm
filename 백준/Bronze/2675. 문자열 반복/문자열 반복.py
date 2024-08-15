T = int(input())
R = 0
text = ''
sentence = []

for i in range(T):
  S = list(map(str,input()))
  R = int(S[0])
  del S[1]
  del S[0]
  text = ''

  for i in S:
    text += i*R

  sentence.append(text)

for i in sentence:
  print(i)