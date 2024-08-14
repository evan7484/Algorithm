text = list(map(str,input()))
if text[0] == ' ' and text[-1] == ' ':
  print(text.count(' ')-1)
elif text[0] == ' ':
  print(text.count(' '))
elif text[-1] == ' ':
  print(text.count(' '))
else:   
  print(text.count(' ')+1)