n = int(input())
fl = []

for i in range(n):
  s = list(map(str, input()))
  fl.append(s[0])
  fl.append(s[-1])

for i in range(0,2*n,2):
  print(fl[i]+fl[i+1])