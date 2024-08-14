graph = []
list1 = []
n = 0
i = 0

graph.append(list(map(int,input())))
if (len(graph[0])<2):
  graph[0].insert(0,0)
list1.append(int(graph[0][i])%10)
list1.append(int(graph[0][i+1])%10)
n1 = int(list1[i])%10
n2 = int(list1[i+1])%10
n3 = (n1 + n2)%10
list1.append(n3)
n += 1
    

number = list1[1]+(list1[0]*10)
cycle = list1[-1]+(list1[-2]*10)

while (number!=cycle):
    n1 = int(list1[i+1])%10
    n2 = int(list1[i+2])%10
    n3 = (n1 + n2)%10
    list1.append(n3)
    n += 1
    i += 1
    cycle = list1[-1]+(list1[-2]*10)


print(n)


