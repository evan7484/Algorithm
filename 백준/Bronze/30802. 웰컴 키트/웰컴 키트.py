# 30802번
import math

N = int(input())
tShirt = list(map(int,input().split()))
T,P = map(int,input().split())

tShirt_num = 0
for i in tShirt:
    n = (i-1)//T + 1
    tShirt_num += n

print(tShirt_num)
print(N//P, N%P)
