def factorial(N):
  n = 1
  if N > 0:
    n = N * factorial(N-1)
  return n
    
N = int(input())
print(factorial(N))
