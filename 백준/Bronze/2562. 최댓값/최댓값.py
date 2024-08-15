list1 = []
list2 = []
for i in range(9):
  num = int(input())
  list1.append(num)
list2 = list1[:]
list1.sort()
print(list1[-1])
print(list2.index(list1[-1])+1)
