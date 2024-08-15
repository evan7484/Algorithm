def d(n):
  list1 = []
  list1.append(str(n))
  sum = n
  for i in range(len(list1[0])):
    sum += int(list1[0][i])
  return sum

huge = []
number = []
for i in range(1,10001):
  number.append(d(i))
  huge.append(i)

number_set = set(number)
number = list(number_set)
number.sort()

rmove = []

for i in range(len(number)):
  if number[i]>10000:
    rmove.append(number[i])
for i in range(len(rmove)):
  number.remove(rmove[i])  
for i in range(len(number)):
  huge.remove(number[i])
for i in range(len(huge)):
  print(huge[i])