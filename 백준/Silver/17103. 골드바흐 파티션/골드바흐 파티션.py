
#소수 골라내기 (에라토스테네스의 체 활용)
primeNum = [False, False] + [True]*999999

for i in range(2, 1000001):
    if primeNum[i]:
        for j in range(i*2, 1000001, i):
            primeNum[j] = False

T = int(input())

#문제 풀이
for i in range(T):
    count = 0
    N = int(input())
    for j in range(2, N//2+1):
        if primeNum[j] and primeNum[N-j]:
            count += 1
    print(count)