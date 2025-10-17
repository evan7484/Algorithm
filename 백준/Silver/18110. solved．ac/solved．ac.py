# 18110번

n = int(input())
difficulty = []
if n == 0:
    print(0)
    exit()

for i in range(n):
    difficulty.append(int(input()))

difficulty.sort()
num = int((n*15)/100 + 0.5)

average = sum(difficulty[num:n - num]) / (n - 2 * num)
print(int(average+0.5))
