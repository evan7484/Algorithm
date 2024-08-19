n = int(input())
dot = list(map(int,input().split()))
answer = dot
dot2 = set(dot)
dot = list(dot2)
dot.sort()
dic = {}
for i in range(len(dot)):
  dic[dot[i]] = i

for i in answer:
  print(dic[i],end = ' ')