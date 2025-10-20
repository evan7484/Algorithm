# 2609번

a, b = map(int,input().split())

gcd = 0

if a > b:
    big = a
    small = b
else:
    big = b
    small = a

#최대공약수 구하기
while True:
    c = big % small
    if c == 0:
        gcd = small
        break
    else:
        big = small
        small = c

print(gcd)
print(int(a *(b/gcd)))