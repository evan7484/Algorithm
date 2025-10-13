# 7568번

N = int(input())
big = []
for i in range(N):
    w,h = map(int,input().split())
    big.append([w,h])

result = []
for i in range(N):
    count = 0
    for j in range(N):
        if big[j][0] > big[i][0] and big[j][1] > big[i][1]:
            count += 1
    result.append(count+1)

for i in result:
    print(i,end =" ")
