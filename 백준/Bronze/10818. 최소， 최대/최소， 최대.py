n = int(input())
maxmin1 = []
maxmin2 = []
i = 0
maxmin1.append(list(map(int,input().split())))
for i in range(len(maxmin1[0])):
  maxmin2.append(maxmin1[0][i]) 

maxmin2.sort()
print(maxmin2[0], maxmin2[-1])

