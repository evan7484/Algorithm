#인사성 밝은 곰곰이

N = int(input())
n = 0
result = []
for i in range(N):
  greet = input()
  if greet == 'ENTER':
    n += 1
  elif greet != 'ENTER':
    greet += str(n)
    result.append(greet)
  
result = set(result)
result = list(result)
print(len(result))

