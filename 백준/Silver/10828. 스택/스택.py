# 10828번

N = int(input())
stack = []
result = []

for i in range(N):
    x = 1
    command = list(map(str,input().split()))
    if command[0] == "push":
        x = int(command[1])
        stack.append(x)
    elif command[0] == "size":
        result.append(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            result.append(1)
        else:
            result.append(0)
    elif len(stack) == 0:
        result.append(-1)
    elif command[0] == "pop":
        result.append(stack.pop())
    elif command[0] == "top":
        result.append(stack[-1])

for i in result:
    print(i)

