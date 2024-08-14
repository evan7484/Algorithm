n = int(input())
i = 666

while n != 0:
  if '666' in str(i):
    n -= 1
  if n == 0:
    data = i
    break
  i += 1
  
print(data)