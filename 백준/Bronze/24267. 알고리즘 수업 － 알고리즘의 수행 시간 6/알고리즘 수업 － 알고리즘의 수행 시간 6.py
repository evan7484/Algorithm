n = int(input())
sum = 0

if n%2 == 0:
  for i in range((n-2)//2):
    sum += (n-2-i)*(i+1)
  print(sum*2)
else: 
  for i in range((n-2)//2+1):
    sum += (n-2-i)*(i+1)
  print(sum*2-(((n-2)//2+1)*((n-2)//2+1)))
print(3)
