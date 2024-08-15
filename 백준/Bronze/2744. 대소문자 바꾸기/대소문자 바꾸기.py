# 백준 2744번 대소문자 바꾸기

s = list(map(str,input()))

for i in range(len(s)):
  if s[i].isupper():
    s[i] = s[i].lower()
  else:
    s[i] = s[i].upper()

for i in s:
  print(i,end = '')