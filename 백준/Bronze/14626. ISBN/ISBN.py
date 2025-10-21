# 14626번

ISBN = list(map(str,input()))
target = ISBN.index('*')
result = 0

if target == 12:
    for i in range(12):
        if i%2 == 0:
            result += int(ISBN[i])
        else:
            result += int(ISBN[i])*3
    print((10 - result%10)%10)
else:
    for i in range(13):
        if i == target:
            continue
        elif i%2 == 0:
            result += int(ISBN[i])
        else:
            result += int(ISBN[i])*3
    if target%2 == 0:
        print((10 - result%10)%10)
    else:
        n = 10-result%10
        print((n*7)%10)