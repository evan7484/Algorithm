N, M  = map(int,input().split())
dic = {}
n = 0
for i in range(N):
  text = input()
  dic[text] = i
  
for i in range(M):
  text = input()
  if text in dic:
    
    n += 1

print(n)