def cantor(a,n):
  if n == 1:
    return 
  for i in range(a+n//3, a+(n//3)*2): 
    result[i] = ' '
  cantor(a, n//3)
  cantor(a+n//3*2,n//3)

while True:
  try : 
    N = int(input())
    result = ['-']*(3**N)
    cantor(0,3**N)
    print(''.join(result))
  except:
    break