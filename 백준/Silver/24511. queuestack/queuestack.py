#queuestack
#내가 안 함

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
M = int(input())
C = list(map(int,input().split()))

queue = deque([])
for i in range(N):
    if A[i] == 0: # 큐인 자료구조만 모으기
        queue.append(B[i])

# 배열 C의 원소를 1개 appendleft 할 때마다 pop 연산 수행
for i in range(M):
    queue.appendleft(C[i])
    print(queue.pop(), end= ' ')
