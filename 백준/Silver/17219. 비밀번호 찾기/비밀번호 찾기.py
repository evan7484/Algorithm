# 17219번
import sys

input = sys.stdin.readline

n,m = map(int,input().split())
password = {}

for _ in range(n):
    a,b = map(str,input().split())
    password[a] = b

for _ in range(m):
    a = input().rstrip('\n')
    print(password[a])