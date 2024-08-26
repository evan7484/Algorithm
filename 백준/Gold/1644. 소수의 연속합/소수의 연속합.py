import math

n = int(input())
start = 0
end = 0
count = 0
sum = 0

N = n
array = [True for i in range(N+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
array[0] = False; array[1] = False # 0과 1은 소수가 아니므로 예외처리

# 에라토스테네스의 체 알고리즘
for i in range(2,int(math.sqrt(N)+1)): # 2부터 n의 제곱근까지의 모든 수를 확인하며
  if array[i]: # i가 소수인 경우(남은 수인 경우)
    # i를 제외한 i의 모든 배수를 지우기
    j = 2
    while i * j <= N:
      array[i * j] = False
      j += 1
num = 0
prime = []
for i in array:
  if i:
    prime.append(num)
  num += 1

while 1:
  if sum == n:
    count += 1

  if sum > n:
    sum -= prime[start]
    start += 1
  elif end == len(prime):
    break
  else:
    sum += prime[end]
    end += 1


print(count)
