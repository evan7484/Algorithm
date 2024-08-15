import string

upper = [i for i in string.ascii_uppercase]

call = list(map(str,input()))
time = 0

for i in range(len(call)): 
  if -1 < upper.index(call[i]) <3:
    time += 3
  elif 2 < upper.index(call[i]) < 6:
    time += 4
  elif 5 < upper.index(call[i]) < 9:
    time += 5
  elif 8 < upper.index(call[i]) < 12:
    time += 6
  elif 11 < upper.index(call[i]) < 15:
    time += 7
  elif 14 < upper.index(call[i]) < 19:
    time += 8
  elif 18 < upper.index(call[i]) < 22:
    time += 9
  elif 21 < upper.index(call[i]) < 26 :
    time += 10

print(time)