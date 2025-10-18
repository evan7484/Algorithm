# 1966번

T = int(input())
result = []
for i in range(T):
    N, M = map(int, input().split())
    importance = list(map(int,input().split()))
    count = 0
    num = 0
    del_num = 0
    while 1:
        if importance[count] == max(importance):
            importance[count] = 0
            num += 1
            if count == M:
                result.append(num)
                break
            count -= 1

        if count < len(importance)-1:
            count += 1
        else:
            count = 0

for i in result:
    print(i)