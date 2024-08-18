k = int(input())
Queue = []
sum = 0

for i in range(k):
  n = int(input())
  if n == 0:
    Queue.pop()
  else:  
    Queue.append(n)

for i in Queue:
  sum += i

print(sum)