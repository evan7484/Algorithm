# 1259번

result = []
while 1:
    n = list(map(str,input()))
    if len(n) == 1 and n[0] == "0":
        break
    num = list(n)
    num.reverse()
    for i in range(len(n)):
        if num[i] != n[i]:
            result.append("no")
            break
        elif i == len(n)-1:
            result.append("yes")

for i in result:
    print(i)
