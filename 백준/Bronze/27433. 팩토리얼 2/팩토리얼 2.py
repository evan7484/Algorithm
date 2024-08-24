def factorial(number):
  if number == 1:
    return False
  return number-1

N = int(input())
result = 1
while factorial(N):
  if N == 0:
    break
  result *= N
  N = factorial(N)
  
print(result)
