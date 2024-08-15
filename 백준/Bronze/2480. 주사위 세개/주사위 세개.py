a, b, c = map(int, input().split())

if a == b and b == c:
  print(10000+1000*a)
elif a == b:
  print(1000+100*a)
elif b == c:
  print(1000+100*b)
elif a == c:
  print(1000+100*a)
else:
  if a>b and a>c:
    d = a
  elif b>a and b>c:
    d = b
  else: 
    d = c
  print(100*d)