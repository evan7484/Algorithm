#먼저 듣도못한 딕셔너리에 대입하고 보도못한 리스트에서 이름이 같으면 리스트에 추가하면 될듯

N, M = map(int,input().split())
dic = {}
results = []
for i in range(N):
  Nohear = input()
  dic[Nohear] = 0

for i in range(M):
  Nosee = input()
  if Nosee in dic:
    results.append(Nosee)

results.sort()
print(len(results))
for i in results:
  print(i)
  