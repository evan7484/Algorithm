i = 0
list1 = []
list2 = []
list3 = []
while (1):
  n1 = int(input())
  list1.append(n1%42)
  i += 1
  if i>9:
    break
for n in range(10):
  num = list1.count(list1[n])
  if num > 1:
    list2.append(list1[n])
  elif num < 2:
    list3.append(list1[n])

set1 = set(list2)
list2 = list(set1)

print(len(list2)+len(list3))