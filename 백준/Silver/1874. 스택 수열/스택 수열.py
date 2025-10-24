# 1874번

n = int(input())
stack = [1]
form = []
result = ['+']

for i in range(n):
    form.append(int(input()))

num = 0
i = 1
while 1:
    if len(stack) == 0:
        stack.append(1)

    if stack[-1] < form[num]:
        i += 1
        stack.append(i)
        result.append('+')
    elif stack[-1] == form[num]:
        stack.pop()
        result.append('-')
        num += 1

        if num == n:
            for i in result:
                print(i)
            break
    else:
        print('NO')
        break