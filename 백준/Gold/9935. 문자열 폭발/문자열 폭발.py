#백준 9935번 문자열 폭발

import sys
x = list(map(str,input().strip()))
M = list(map(str,input().strip()))
m = len(M)
bomb = []
for i in x:
    bomb.append(i)
    if bomb[len(bomb)-m:len(bomb)] == M: #스택의 끝부터 M의 글자열 크기까지 자른게 M과 같다면
        for _ in range(m): # m의 길이만큼
            bomb.pop() # stack에서 꺼내준다!
if bomb:
    print(*bomb, sep='')
else:
    print("FRULA")
