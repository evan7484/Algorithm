N = int(input())
enterlog = {}

for i in range(N):
  name, log = map(str,input().split())
  enterlog[name] = log
  
results = list(enterlog.values()) 
results2 = list(enterlog.keys())

pprint = []

for i in range(len(results)):
  if results[i] == 'enter':
    pprint.append(results2[i])

pprint.sort(reverse = True)
for i in pprint:
  print(i)