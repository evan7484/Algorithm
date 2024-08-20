a,b,c,d,e,f = map(int,input().split())
#((b*d)-(e*a))y = c*d - f*a
for i in range(-999,1000):
  for j in range(-999,1000):
    if a*i + b*j == c and d*i + e*j == f:
      print(i,j)
      break