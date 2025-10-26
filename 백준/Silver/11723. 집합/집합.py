# 11723번
import sys
input = sys.stdin.readline

M = int(input())
S = set()

for i in range(M):
    calc = list(map(str,input().split()))
    if calc[0] == 'add':
        S.add(int(calc[1]))
    elif calc[0] == 'remove':
        S.discard(int(calc[1]))
    elif calc[0] == 'check':
        if int(calc[1]) in S:
            print(1)
        else:
            print(0)
    elif calc[0] == 'toggle':
        if int(calc[1]) in S:
            S.remove(int(calc[1]))
        else:
            S.add(int(calc[1]))
    elif calc[0] == 'all':
        S = set(map(int, range(1, 21)))
    elif calc[0] == 'empty':
        S.clear()