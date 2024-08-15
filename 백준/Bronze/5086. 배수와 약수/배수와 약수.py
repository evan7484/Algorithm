a = 1; b= 1
printf = []

while True:
  a, b = map(int,input().split())
  if a == 0 and b == 0:
    break
  
  if b%a == 0:
    printf.append('factor')
  elif a%b == 0:
    printf.append('multiple')
  else:
    printf.append('neither')

for i in printf:
  print(i)
