def factorial(n):
  if n <= 1: # n이 1 이하인 경우 1을 반환
    return 1
  # n! = n * (n - 1)!를 그대로 코드 작성하기
  return n * factorial(n-1)


N,K = map(int,input().split())

result = factorial(N)//(factorial(K)*factorial(N-K))
print(result)