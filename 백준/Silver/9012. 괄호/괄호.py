#여는 괄호와 닫는 괄호의 개수도 같아야하며 닫는 괄호가 여는 괄호보다 먼저 나와서는 안된다
T = int(input())
result = []

for i in range(T):
  Ps = list(map(str,input()))
  for i in range(len(Ps)):
    if Ps[0] != '(' or ')' not in Ps:
      result.append('NO')
      break
    del Ps[0]
    
    if ')' in Ps:
      Ps.remove(')')
      if len(Ps) == 0:
        result.append('YES')
        break

for i in result:
  print(i)
