import string

lower = [i for i in string.ascii_lowercase]

alphabet = list(map(str,input()))
words = 0

for i in range(len(alphabet)):
  n = len(alphabet)
  words += 1
  m = 0
  if i + 1 < n:
    if alphabet[i] == 'd':
      if alphabet[i+1] == 'z' and i+1 == n-1:
        1
      elif alphabet[i+1] == 'z' and i+2 <= n:
        if alphabet[i+2] not in lower:
          words -= 1
      elif alphabet[i+1] == '-':
        words -= 1
    elif alphabet[i] == 'l' or alphabet[i] == 'n':
      if alphabet[i+1] == 'j':
        words -= 1
    elif alphabet[i] == 's' or alphabet[i] == 'c':
      if alphabet[i+1] == '=':
        words -= 1
      elif alphabet[i+1] == '-':
        words -= 1
    elif alphabet[i] == 'z':
      if alphabet[i+1] == '=':
        words -= 1
  
print(words)

